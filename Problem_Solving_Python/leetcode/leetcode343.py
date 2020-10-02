class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(n+1)]
        dp[0] = [1 for _ in range(n+1)]
        for row in dp:
            row[0] = 1
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(1, n+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-i]*i)
        return dp[n][n]