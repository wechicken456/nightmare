#!/usr/bin/python3

from z3 import *

expected = [0x41, 0x29, 0xd9, 0x65, 0xa1, 0xf1, 0xe1, 0xc9, 0x19, 0x09, 0x93, 0x13, 0xa1, 0x09, 0xb9, 0x49, 0xb9, 0x89 , 0xdd, 0x61, 0x31, 0x69, 0xa1, 0xf1, 0x71, 0x21 , 0x9d, 0xd5, 0x3d, 0x15, 0xd5]

def not_op(char):
	result = ""
	char = bin(char)[2:]			
	char = "0"*(8-len(char)) + char		# add 0s to the front to make it 8-bit
	for i in char:
		if i == "0":
			result += "1"
		else:
			result += "0"
	return int("0b"+result, 2)

def bit_shift(char):
	x = ((char >> 1) & 0x55) | ((char & 0x55)*2)
	y = ((x >> 2) & 0x33) | ((x & 0x33) << 2)
	result = (y >> 4) | (y << 4)
	result &= 0xff
	return result

before_not = []
z = Solver()
for i in expected:
	before_not.append(not_op(i))			# reverse the `not` operation

test_bytes = []
for i in range(len(expected)):
	byte = BitVec("%d" % i, 16)
	test_bytes.append(byte)

for i in range(len(expected)):
	z.add(bit_shift(test_bytes[i]) == before_not[i])

flag = []
if z.check() == sat:
	solution = z.model()
	for i in range(len(expected)):
		flag.append(chr(int(str(solution[test_bytes[i]]))))
	print ("".join(flag)[::-1])				# reverse it cause the original flag was reversed
