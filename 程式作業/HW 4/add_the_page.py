test_case = int(input())

for i in range(test_case):
    n = int(input())
    if n == 0:
        break
    sum = 0
    total_page = 0
    for j in range(1000000):
        sum += j
        if sum > n:
            total_page = j
            break
    lost_page = sum - n
    print(lost_page, total_page)