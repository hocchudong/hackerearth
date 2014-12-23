# What is the string made of?

a = raw_input()
kq = 0
for i in range(len(a)):
    b = int(a[i])
    if b in [0,6,9]:
        kq += 6
    elif b == 1:
        kq += 2
    elif b in [2,3,5]:
        kq += 5
    elif b == 4:
        kq += 4
    elif b == 8:
        kq += 7
    else:
        kq += 3
print kq
