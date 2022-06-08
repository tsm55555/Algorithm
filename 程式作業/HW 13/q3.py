from math import sqrt

n = int(input())

ans = {}
print(n, '=', sep='', end='')
while 1:
    for i in range(2, int(sqrt(n)+1)):
        if n%i == 0:
            # print(i, '*')
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1
            n = int(n/i)
            break
    else:
        # print(n)
        if n in ans:
            ans[n] += 1
        else:
            ans[n] = 1
        # print(len(ans))
        count = 1
        for i in ans:
            if ans[i] > 1:
                print(i, '^', ans[i], sep='', end='')
            else:
                print(i, sep='', end='')
                
            if count != len(ans):
                print('*', sep='', end='')
            count += 1
        break