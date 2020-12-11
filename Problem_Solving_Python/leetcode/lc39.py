# https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        li = []
        n = len(candidates)
        combination = []
        candidates.sort()

        def helper(start, summ):
            if summ == target:
                li.append(combination[:])
                return

            if summ > target:
                return

            for i in range(start, n):
                combination.append(candidates[i])
                helper(i, summ+candidates[i])
                combination.pop(-1)

        helper(0,0)
        return li