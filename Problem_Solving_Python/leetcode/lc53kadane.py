from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_so_far = nums[0]
        max_ending_here = nums[0]
        for i in range(1, n):
            max_ending_here = max(nums[i], nums[i]+max_ending_here)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far