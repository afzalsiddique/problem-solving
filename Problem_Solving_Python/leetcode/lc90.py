# https://leetcode.com/problems/subsets-ii/
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        combination = []
        n = len(nums)
        nums.sort()
        def backtrack(start):
            res.append(combination[:])
            for i in range(start, n):
                if i>start and nums[i] == nums[i-1]:
                    continue
                combination.append(nums[i])
                backtrack(i+1)
                combination.pop(-1)
        backtrack(0)
        return res