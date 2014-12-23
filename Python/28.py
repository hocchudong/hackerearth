# A Needle in the Haystack

a = input()
kq = []
for i in range(a):
    b = raw_input()
    c = raw_input()
    if (b in c) or (b[::-1] in c):
        kq.append("YES")
    else:
        kq.append("NO")
for i in kq:
    print i
