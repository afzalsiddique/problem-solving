from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n==1:
            return nums[0]
        burstAll = float('-inf')
        for i in range(n):
            left = nums[:i]
            right = nums[i+1:]
            balloons_after_burst = left+right
            if i == 0:
                burstCurrent = nums[0] * nums[1]
            elif i == n-1:
                burstCurrent = nums[n-1] * nums[n-2]
            else:
                burstCurrent = nums[i-1] * nums[i] * nums[i+1]
            burstNext = self.maxCoins(balloons_after_burst)
            burstAll = max(burstAll, burstCurrent + burstNext)
        return burstAll


