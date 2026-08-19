n, target_number = map(int, input().split())

nums = []
dp = [0 for _ in range(target_number + 1)]

for i in range(n):
    nums.append(int(input()))

dp[0] = 1

for num in nums:
    for coin in range(num , target_number + 1):
        dp[coin] += dp[coin - num]
print(dp[target_number])