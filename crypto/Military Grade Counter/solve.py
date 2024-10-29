from pwn import *

context.log_level = 'error'

def get_conn():
    io = remote('127.0.0.1', 5069)
    return io

def __xor(sa, sb):
    return bytes([a^b for a, b in zip(sa, sb)])

def __get_blocks(pt):
    blocks = []
    for i in range(0, len(pt), 16):
        blocks.append(pt[i : i + 16])
    return blocks

io = get_conn()
io.recvuntil(b': ')
ct = __get_blocks(bytes.fromhex(io.recvline().decode().strip()))
sz = len(ct)

io.recvuntil(b': ')
to_send = b'\x00'*16*275
io.sendline(to_send.hex().encode())
stream_blocks = __get_blocks(bytes.fromhex(io.recvline().decode().strip().split(': ')[-1]))

j = 0
flag = ''
for i in range(256 - sz, 256):
    m = __xor(ct[j], stream_blocks[i])
    flag += m.decode()
    j += 1

print(flag)
