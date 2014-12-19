#Crazy kangaroo

a = input()
fn = []
for i in range(a):
    a = raw_input().split()
    for i in range(len(a)):
        a[i] = int(a[i])

    x = a[0] / a[2]
    y = a[1] / a[2]

    if a[0] % a[2]:
        x += 1
    
    kq = y - x + 1
    fn.append(kq)

for i in fn:
    print i
