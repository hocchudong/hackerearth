#Date With Avni

kq = []
a = input()
for i in range(a):
    dem = 0
    b = raw_input()
    for j in range(len(b) - 1):
        if b[j] <> b[j + 1]:
            dem += 1
    if dem == len(b) - 1:
        kq.append("KISS")
    else:
        kq.append("SLAP") 

for i in kq:
    print i



	
