def count_uphill_numbers(N):
    MOD = 10007
    dp = [[0] * 10 for _ in range(N + 1)]

    for j in range(10):
        dp[1][j] = 1

    for i in range(2, N + 1):
        for j in range(10):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j] if j > 0 else dp[i - 1][j]
            dp[i][j] %= MOD  

    return sum(dp[N]) % MOD

N = int(input())
print(count_uphill_numbers(N))
