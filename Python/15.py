# Hell of a Day
n = input()
a = raw_input()
lst = list(map(lambda x: int(x), a.split()))
odd = []
even = []
for i in lst:
    if i % 2:
        odd.append(i)
    else:
        even.append(i)
odd.sort()
even.sort()
even = even[::-1]

for i in even:
    print i,
print
for i in odd:
    print i,
