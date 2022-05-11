testcase_num = int(input())

for i in range(testcase_num):
    n, p = list(map(int, input().split()))
    k = pow(p, 1/n)
    print(round(k))