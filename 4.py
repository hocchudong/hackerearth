# Roy and Profile Picture

L = input()
N = input()

chuoi1 = []
chuoi2 = []

def sosanh(a,b):
    if a < L or b < L:
        chuoi2.append("UPLOAD ANOTHER")
    elif a == b:
        chuoi2.append("ACCEPTED")
    else:
        chuoi2.append("CROP IT")

for i in range(N):
    chuoi1 = raw_input().split()
    x = int(chuoi1[0])
    y = int(chuoi1[1])
    sosanh(x,y)

for i in chuoi2:
    print i


