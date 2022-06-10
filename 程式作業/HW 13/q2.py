# from math import gcd 

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)

def Euler(n):
    count = 1
    for i in range(2, n):
        if gcd(n, i) == 1:
            count += 1
    return count

test_num = int(input())

for i in range(test_num):
    n = int(input())
    ans = Euler(n)
    print(ans)