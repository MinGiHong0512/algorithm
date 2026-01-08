n = int(input())

stair = [0 for _ in range(n)]
dp = [0 for _ in range(n)]


for i in range(n):
    stair[i] = int(input())

dp[0] = stair[0]

if n >= 2:
    dp[1] = stair[1] + stair[0]

    for i in range(2,n):
        if stair[i] + dp[i-2] > stair[i] + stair[i-1] + dp[i-3]:
            dp[i] = stair[i] + dp[i-2]
        else:
            dp[i] = stair[i] + stair[i-1] + dp[i-3]

print(dp[n-1])