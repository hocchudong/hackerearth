# Small Factorials

abc = []
a = input()
for i in range(a):
    b = input()
    abc.append(b)

for i in abc:
    kq = 1
    for x in range(1,i+1):
        kq *= x
    print kq
