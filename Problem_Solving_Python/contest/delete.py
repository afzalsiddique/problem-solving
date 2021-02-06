from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def helper(nums):
            n = len(nums)
            if n == 1:
                return nums[0], 1
            if n == 2:
                if nums[0] == nums[1]:
                    return nums[0], 2
                else:
                    return 'none', 0
            mid = n // 2
            left = nums[:mid]
            right = nums[mid:]
            maj_left, extra_left = helper(left)
            maj_right, extra_right = helper(right)
            if maj_right == maj_left:
                return maj_right, extra_left + extra_right
            elif extra_left > extra_right:
                return maj_left, extra_left - extra_right
            else:
                return maj_right, extra_right - extra_left

        return helper(nums)[0]
