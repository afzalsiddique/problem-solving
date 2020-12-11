# https://leetcode.com/problems/house-robber-ii/discuss/59934/Simple-AC-solution-in-Java-in-O(n)-with-explanation/61023
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(nums):
            n = len(nums)
            prev_yes, prev_no = 0, 0
            for i in range(n):
                prev_yes, prev_no = max(prev_yes, prev_no), nums[i] + prev_yes
            return max(prev_yes, prev_no)

        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        if n == 3: return max(nums[0], nums[1], nums[2])
        return max(helper(nums[1:]), nums[0] + helper(nums[2:-1]))
