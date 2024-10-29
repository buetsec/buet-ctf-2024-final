#!/usr/local/bin/python

import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

class COUNTER():
    def __init__(self, key, iv):
        self.key, self.iv = key, iv
        self.block_size = 16
        self.counter = 0

    def __get_blocks(self, pt):
        blocks = []
        for i in range(0, len(pt), self.block_size):
            blocks.append(pt[i : i + self.block_size])
        return blocks
    
    def __xor(self, sa, sb):
        return bytes([a^b for a, b in zip(sa, sb)])
    
    def __encrypt(self, block):
        stream = AES.new(key, AES.MODE_ECB).encrypt(
                    iv + int(self.counter & 0xFF).to_bytes(2, 'big'))
        self.counter += 1
        return self.__xor(block, stream)

    def encrypt(self, pt):
        blocks = self.__get_blocks(pad(pt, self.block_size))
        ct = []
        for block in blocks:
            ct.append(self.__encrypt(block).hex())
        return ''.join(block for block in ct)
    

print('Welcome to my next gen military grade symmetric encryption!!')

key, iv = os.urandom(16), os.urandom(14)
cipher = COUNTER(key, iv)

enc = cipher.encrypt(open('flag.txt', "rb").read())
print(f'Have an encrypted flag: {enc}')

pt = bytes.fromhex(input('Let me encrypt for you this one time: '))
ct = cipher.encrypt(pt)
print(f'Here you go: {ct}')