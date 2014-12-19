#Life, the Universe, and Everything

b = []
while True:
    a = input()
    b.append(a)
    if 42 in b:
        break

for i in b[0:-1]: 
    print i
