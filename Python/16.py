#Palindromic Numbers

n = input()
def check_palindromic(x):
    if str(x) == str(x)[::-1]:
        return True
    return False

kq = []
for i in range(n):
    dem = 0
    nhap = list(map(lambda x: int(x), raw_input().split()))
    for j in range(nhap[0], nhap[1]+1):
        if check_palindromic(j) == True:
            dem += 1
    kq.append(dem)
for i in kq:
    print i
    
