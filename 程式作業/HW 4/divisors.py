def count_divisor(n):
    x = 0
    sqrt_n = int(n**0.5)
    if sqrt_n**2 == n:
        x -= 1
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            x += 1
    x *= 2
    return x

test_case = int(input())

for i in range(test_case):
    num = list(map(int,input().split())) 
    L = num[0]
    U = num[1]
    maximum  = 0
    divisors = 0
    for i in range(L,U+1):
        current_divisors = count_divisor(i)
        # print(i, "have", current_divisors, "divisors.")
        if current_divisors > divisors:
            divisors = current_divisors
            maximum = i        
    print("Between ", L, " and ", U,", ", maximum, " has a maximum of ", divisors, " divisors.", sep='')