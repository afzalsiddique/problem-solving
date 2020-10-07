def num_of_tilings(W) -> int:
    dp = [[0] * 16 for _ in range(W + 1)]
    dp[0][15] = 1
    for i in range(1, W + 1):
        dp[i][0] += dp[i - 1][0]
        dp[i][0] += dp[i - 1][3]
        dp[i][0] += dp[i - 1][9]
        dp[i][0] += dp[i - 1][12]
        dp[i][0] += dp[i - 1][15]

        dp[i][3] += dp[i - 1][0]
        dp[i][3] += dp[i - 1][3]
        dp[i][3] += dp[i - 1][9]
        dp[i][3] += dp[i - 1][12]
        dp[i][3] += dp[i - 1][15]

        dp[i][6] += dp[i - 1][0]
        dp[i][6] += dp[i - 1][3]
        dp[i][6] += dp[i - 1][9]
        dp[i][6] += dp[i - 1][12]
        dp[i][6] += dp[i - 1][15]

        dp[i][9] += dp[i - 1][6]

        dp[i][12] += dp[i - 1][0]
        dp[i][12] += dp[i - 1][3]
        dp[i][12] += dp[i - 1][9]
        dp[i][12] += dp[i - 1][12]
        dp[i][12] += dp[i - 1][15]

        dp[i][15] += dp[i - 1][0]
        dp[i][15] += dp[i - 1][3]
        dp[i][15] += dp[i - 1][6]
        dp[i][15] += dp[i - 1][9]
        dp[i][15] += dp[i - 1][12]
        dp[i][15] += dp[i - 1][15]

    return dp[W][15]

