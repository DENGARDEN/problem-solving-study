def solution(m, n, puddles):
    MOD = 1000000007
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif [j+1, i+1] in puddles:  # 1-indexed로 변환
                dp[i][j] = 0
            elif i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

    return dp[n-1][m-1] % MOD