from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums))

    def get_right_max(self, nums, l, r):
        right_max, temp = float('-inf'), 0
        for i in range(l, r):
            temp += nums[i]
            right_max = max(temp, right_max)
        return right_max

    def get_left_max(self, nums, l, r):
        left_max, temp = float('-inf'), 0
        for i in range(r - 1, l - 1, -1):
            temp += nums[i]
            left_max = max(temp, left_max)
        return left_max

    def helper(self, nums: List[int], l, r) -> int:
        if l == r - 1:
            return nums[l]
        mid = l + (r - l)//2
        max_left = self.get_left_max(nums, l, mid)
        max_right = self.get_right_max(nums, mid, r)
        max_cross = max_left + max_right

        half_left = self.helper(nums, l, mid)
        half_right = self.helper(nums, mid, r)
        return max(half_left, half_right, max_cross)
