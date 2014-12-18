a = input()
b = raw_input().split()
for i in range(0,len(b)):
	b[i] = int(b[i])

dem = 1

b.sort()
"""c = b[::-1]

for i in range(len(c)):
	for j in range(dem):
		if c[j] == 0:
			continue
		else:
			c[j] -= 1
	dem += 1
	
print dem + 2"""
