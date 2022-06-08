test_num = int(input())

for i in range(test_num):
    num = list(map(int, input().split()))
    num.sort()
    k = int(input())
    print(num[k-1])
