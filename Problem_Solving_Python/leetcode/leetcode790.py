class Solution:
    def numTilings(self, N: int) -> int:
        mod = 1000000007
        dp = [[0]*4 for _ in range(N+1)]
        dp[0][3] = 1
        for i in range(1, N+1):
            dp[i][0] += dp[i-1][3] % mod

            dp[i][1] += dp[i-1][0] % mod
            dp[i][1] += dp[i-1][2] % mod

            dp[i][2] += dp[i-1][0] % mod
            dp[i][2] += dp[i-1][1] % mod

            dp[i][3] += dp[i-1][0] % mod
            dp[i][3] += dp[i-1][1] % mod
            dp[i][3] += dp[i-1][2] % mod
            dp[i][3] += dp[i-1][3] % mod

        return dp[N][3] % mod
