from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for i in range(n-1):
            j = i + 1
            dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        for i in range(n-3, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = max(dp[i][j-1], dp[i][j-2] + nums[j])
        return dp[0][-1]
