class Solution:
    def fib(self, N: int) -> int:
        dp = [0]*N
        def helper(n):
            if n==0:
                return 0
            if n==1:
                return 1
            last = helper(n-1)
            secondlast = helper(n-2)
            dp[n-1] = last
            dp[n-2] = secondlast
            return last+secondlast
        return helper(N)