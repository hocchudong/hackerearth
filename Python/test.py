# Reverse Primes
from math import sqrt

def check_prime(x):
    a = 2
    while a <= sqrt(x):
        if not x % a:
            return False
        else:
            a += 1
    return True


tem = []
k = 3
while k < 10**15:
    if check_prime(k) == True:
        tem.append(k)
    else:
        k += 1

for i in tem:
    if str(i)[::-1] in tem and i < int(str(i)[::-1]):
        print i



