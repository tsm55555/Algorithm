test_num = int(input())

for i in range(test_num):
    N, S = list(map(int, input().split()))
    if not N and not S:
        break
    denomination = list(map(int, input().split()))
    dp = []
    dp.append(0)
    for i in range(1, S+1):
        dp.append(float("inf"))
    for i in range(1, S+1):
        # print("i", i)
        for coin in denomination:
            # print("coin", coin)
            if i >= coin:
                dp[i] = min(dp[i-coin]+1, dp[i])
    # print(dp)
    print(dp[S])