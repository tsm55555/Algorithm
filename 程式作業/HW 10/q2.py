test_num = int(input())


for i in range(test_num):
    m, n = list(map(int, input().split()))
    ans = 2**m + 2**n
    print(ans)