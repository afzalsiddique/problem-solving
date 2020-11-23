from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        di = {}
        return self.helper(nums, di)

    def helper(self, nums: List[int], di) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        burstAll = float('-inf')
        for i in range(n):
            balloons_after_burst = nums[:i] + nums[i + 1:]
            if i == 0:
                burstCurrent = nums[0] * nums[1]
            elif i == n - 1:
                burstCurrent = nums[n - 1] * nums[n - 2]
            else:
                burstCurrent = nums[i - 1] * nums[i] * nums[i + 1]

            if tuple(balloons_after_burst) in di:
                burstNext = di[tuple(balloons_after_burst)]
            else:
                burstNext = self.helper(balloons_after_burst, di)
            burstAll = max(burstAll, burstCurrent + burstNext)

        di[tuple(nums)] = burstAll
        return burstAll
