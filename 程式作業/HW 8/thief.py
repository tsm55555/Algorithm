testcase_num = int(input())

for i in range(testcase_num):
    T, N = list(map(int, input().split()))
    M = list(map(int, input().split()))
    for j in range(N):
        sum = 0
        taken = []
        is_possible = False
        for k in range(j, N):
            sum += M[k]
            if(sum > T):
                sum -= M[k]
            else:
                taken.append(M[k])

            if(sum == T):
                print(*taken)
                is_possible = True
                break
        if(is_possible):
            break
    if not is_possible:
        print("impossible")