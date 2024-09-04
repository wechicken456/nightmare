
x = ["Dufhbmf", "pG`imos", "ewUglpt"]

flag = ""
for i in range(0xc):
	for j in range(32,127):
		if ord(x[i%3][int(i/3)*2]) - j == 1:
			flag += chr(j)
			break

print(flag)
