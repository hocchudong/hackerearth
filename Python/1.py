# The best Internet Brower

a = input()
abc = []
for i in range(a):
    web = raw_input()
    abc.append(web)

def nhap(x):
    b = x[4:-4]
    c = []
    for i in b:
        if i not in ["u","e","o","a","i"]:
            c.append(i)
        else:
            pass
    d = len(c)
    kq = len(c) + 4
    tong = len(x)
    print str(kq) + "/" + str(tong)

a = raw_input()
nhap(a)

for i in abc:
    nhap(i)
