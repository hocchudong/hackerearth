#Crazy kangaroo

a = input()
fn = []
for i in range(a):
    a = list(map(lambda x: int(x), raw_input().split()))

    x = a[0] / a[2]
    y = a[1] / a[2]

    if a[0] % a[2]:
        x += 1
    
    kq = y - x + 1
    fn.append(kq)

for i in fn:
    print i
