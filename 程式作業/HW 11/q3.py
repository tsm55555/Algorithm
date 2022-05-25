test_num = int(input())

for i in range(test_num):
    num = int(input())
    n = (num-1)/2 + 1
    last = 1 + 2 * (n**2 - 1)
    ans = last**3 - 6*last**2 + 8*last
    print(int(ans))