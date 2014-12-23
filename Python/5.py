# Gotta catch 'em all!

a = input()
b = list(map(lambda x: int(x), raw_input().split()))

dem = 1

b.sort()
c = b[::-1]

dem = 0
kq1 = 0
for i in c:
    kq = i + 2 + dem
    dem += 1
    if kq > kq1:
        kq1 = kq

print kq1
