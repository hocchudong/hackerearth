a = input()
tem = []
kq = []
for i in range(a):
    b = raw_input()
    tem.append(b)

for j in tem:
    print j
    if j[::-1] in tem:
    	kq.append(str(len(j)))
    	kq.append(j[len(j)/2])
    	break
    else:
        continue

print kq[0] + " " + kq[1] 
