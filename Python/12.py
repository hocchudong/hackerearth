# Minimal Combinatorial

from math import factorial
kq = []
for i in (range(input())):
    a = raw_input().split()
    kq.append( factorial( int(a[0]) ) / ( factorial( int(a[1]) ) * factorial( int(a[0]) - int(a[1]) ) ) )
for i in kq: print i
