# Girlfriend's demands

a = raw_input()
b = input()
     
chuoi1 = []
chuoi2 = []
     
def sosanh(a1,b1):
    if a1 == b1:
        chuoi2.append("Yes")
    else:
        chuoi2.append("No")
     
for i in range(b):
    chuoi1 = raw_input().split()
    x1 = int(chuoi1[0])
    y1 = int(chuoi1[1])
    x2 = x1 % len(a) - 1
    y2 = y1 % len(a) - 1
    x3 = a[x2]
    y3 = a[y2]
    sosanh(x3,y3)
     
for i in chuoi2:
    print i
