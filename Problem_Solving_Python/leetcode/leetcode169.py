from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums))[0]

    def helper(self, nums, l, r):
        if l == r - 1:
            return nums[l], 1
        mid = l + (r - l) // 2
        maj_left, extra_left = self.helper(nums, l, mid)
        maj_right, extra_right = self.helper(nums, mid, r)

        if maj_right==maj_left:
            maj = maj_left
            extra = extra_left + extra_right
        elif extra_right > extra_left:
            maj = maj_right
            extra = extra_right - extra_left
        else:
            maj = maj_left
            extra = extra_left - extra_right
        return maj, extra
