from Crypto.Util.number import long_to_bytes as l2b, isPrime, GCD
from pwn import *
from functools import reduce

context.log_level = 'error'

def get_conn():
    io = remote('127.0.0.1', 5420)
    return io

def query1(io, i, j, m):
    io.recvuntil(b': ')
    io.sendline(b'1')

    io.recvuntil(b': ')
    io.sendline(str(i).encode() + b' ' + str(j).encode())
    io.recvuntil(b': ')
    io.sendline(str(m).encode())
    return int(io.recvline().decode().strip().split('= ')[-1])

def query2(io):
    io.recvuntil(b': ')
    io.sendline(b'2')
    return int(io.recvline().decode().strip().split('= ')[-1])

def clean(x):
    for d in range(2, 10000):
        while x % d == 0:
            x = x // d
    return x

def get_prime(ct1, ct2):
    e = 0x10001
    l1 = (2**e) - ct1
    l2 = (2**e) - ct2

    l1, l2 = clean(l1), clean(l2)
    
    p = GCD(l1, l2)
    p = clean(p)
    assert isPrime(p)
    return p

def decrypt(ct, p, q):
    e = 0x10001
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    return pow(ct, d, p * q)

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * pow(p, -1, n_i) * p
    return sum % prod

def get_flag(ct1, ct2, primes):
    e = 0x10001
    for i in range(3):
        for j in range(3):
            msg1 = decrypt(ct1, primes[i], primes[j])
            if i == j: continue
            for k in range(3):
                for l in range(3):
                    if k == l: continue
                    if i == k or j == k: continue
                    msg2 = decrypt(ct2, primes[k], primes[l])
                    msg = l2b(chinese_remainder([primes[i], primes[j], primes[k]], [msg1 % primes[i], msg1  % primes[j], msg2 % primes[k]]))
                    if b'BUETCTF' in msg:
                        return msg
    return -1

def solve(io):
    io.recvline()

    ct1 = query1(io, 0, 1, 2)
    ct2 = query1(io, 7, 2, 2)
    ct3 = query1(io, 8, 3, 2)
    ct4 = query1(io, 9, 4, 2)
    p, q, r = get_prime(ct1, ct2), get_prime(ct2, ct3), get_prime(ct3, ct4)

    ct1 = query2(io)
    ct2 = query2(io)

    flag = get_flag(ct1, ct2, [p, q, r])
    if flag == -1:
        return False
    else:
        print(flag.decode())
        return True

while True:
    print('Trying...')
    if solve(get_conn()):
        break
