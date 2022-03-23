def ugly(n):
    if(n < 6):
        return n

    s = [1]
    n -= 1
    while(n):
        element = min(s)

        index = s.index(element)
        del s[index]
        s = set(s)
        s.add(element * 2)
        s.add(element * 3)
        s.add(element * 5)
        s = list(s)
        n -= 1
    return min(s)

test_case = int(input())

for i in range(test_case):
    n = int(input())
    ans = ugly(n)
    print(ans)