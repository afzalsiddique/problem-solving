# https://www.youtube.com/watch?v=uG_MtaCJIrM
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]  # build the complete array
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for window in range(1, n):
            for left in range(n - window):
                right = left + window
                for k in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right])
        return dp[0][n - 1]