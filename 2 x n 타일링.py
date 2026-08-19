def solution(n):
    answer = 0

    dp = [0 for _ in range(n+1)]

    dp[0] = 1
    dp[1] = 2

    if n >= 2:
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

    answer = dp[n-1]

    return answer % 1_000_000_007


n = int(input())

print(solution(n))