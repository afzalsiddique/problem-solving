class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*n
        def helper(n):
            if n==1:
                return 1
            if n==2:
                return 2
            if dp[n-1] == -1:
                dp[n-1] = helper(n-1)
            if dp[n-2] == -1:
                dp[n-2] = helper(n-2)

            return dp[n-1]+dp[n-2]

        return helper(n)
