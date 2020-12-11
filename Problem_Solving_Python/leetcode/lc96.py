# https://www.youtube.com/watch?v=CMaZ69P1bAc

class Solution:
    def numTrees(self, n: int) -> int:
        def catalan(nth):
            dp = [0]*(nth+1)
            dp[0] = dp[1] = 1
            if nth == 0 or nth == 1: return 1
            for n in range(2, nth + 1):
                for i in range(0, n):
                    dp[n] += dp[i] * dp[n-i-1]
            return dp[nth]

        return catalan(n)

