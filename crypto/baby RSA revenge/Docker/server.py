#!/usr/local/bin/python
from Crypto.Util.number import getPrime, bytes_to_long as b2l, long_to_bytes as l2b
import random

print("Welcome to delphi's query service (Again)!!")

primes = [getPrime(512) for _ in range(6)]

with open('flag.txt', 'rb') as f:
    flag = f.read()
    
m = b2l(flag)
assert(m.bit_length() > 1200 and m.bit_length() < 1500)

used_indices = set()
for _ in range(6):
    op = int(input('Enter the type of operation you want to do: '))

    if op == 1:
        i, j = map(int, input('Enter 2 indices for primes to be used for RSA (eg. 0 4): ').split())
        if i in used_indices or j in used_indices or i < 0 or j < 0 or i == j:
            print('Illegal values given!!')
            exit(2)
            
        i, j = i % 6, j % 6

        if i == j:
            print("Don't try to be too clever mister!")
            exit(2)
        
        used_indices.add(i)
        used_indices.add(j)
        
        p, q = primes[i], primes[j]
        n = p * q
        e = 0x10001

        msg = int(input('Enter what you want to encrypt: '))
        assert 0 < msg < n, "????"

        ct = pow(msg, e, n)
        print('ct = ', ct)

    elif op == 2:
        i, j = 0, 0
        while i == j:
            i, j = random.randint(0, 5), random.randint(0, 5)
        
        p, q = primes[i], primes[j]
        n = p * q
        e = 0x10001

        ct = pow(m, e, n)
        print('ct = ', ct)

    else:
        print('~~Invalid operation~~')
        exit(2)