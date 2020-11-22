from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums))

    def getRightMax(self, nums, l, r):
        rightmax, temp = float('-inf'), 0
        for i in range(l, r):
            temp += nums[i]
            rightmax = max(temp, rightmax)
        return rightmax

    def getLeftMax(self, nums, l, r):
        leftmax, temp = float('-inf'), 0
        for i in range(r - 1, l - 1, -1):
            temp += nums[i]
            leftmax = max(temp, leftmax)
        return leftmax

    def helper(self, nums: List[int], l, r) -> int:
        if (l == r - 1):
            return nums[l]
        n = r - l
        rightmax = self.getRightMax(nums, n // 2, n)
        # print("right:", rightmax)
        leftmax = self.getLeftMax(nums, 0, n // 2)
        # print("left:", leftmax)

        crossmax = leftmax + rightmax

        return max(self.helper(nums, 0, n // 2), self.helper(nums, n // 2, n), crossmax)
