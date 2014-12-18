# Complete String

a = input()
c = []

for i in range(a):
    b = raw_input()
    c.append(b)

mau = "qwertyuioplkjhgfdsazxcvbnm"
for i in c:
    if len(i) < 26:
        print "NO"
    else:
        dem = 0
        for j in mau:
            if j in i:
                dem += 1
        if dem == len(mau):
            print "YES"
        else:
            print "NO"
