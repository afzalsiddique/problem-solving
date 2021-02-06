from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1]*n
        def helper(i):
            if n<0:
                return 0
            if i==1 or i==2:
                return cost[i]
            if dp[i] != -1:
                return dp[i]
            dp[i] = cost[i] + min(helper(i-1), helper(i-2))
            return dp[i]
        return min(helper(n-1), helper(n-2))
