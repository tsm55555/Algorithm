T = int(input())

for i in range(T):
    N = int(input())
    ans = 0
    field = list(input())
    for j in range(N):
        if(field[j] == "."):
            ans += 1
            try:
                field[j+1] = "#"
                field[j+2] = "#"
            except IndexError:
                pass
    print("Case ", i+1, ": ", ans, sep="")