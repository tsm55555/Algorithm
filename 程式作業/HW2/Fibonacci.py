def f(n):
    a = 0;
    b = 1;

    if n == 0:
        return a
    elif n == 1:
        return b

    for i in range(n-1):
        c = a + b
        a = b
        b = c
    return c

test_num = int(input())
ans = []
for i in range(test_num):
    num = int(input())
    ans.append(f(num))

for i in range(test_num):
    print(ans[i])