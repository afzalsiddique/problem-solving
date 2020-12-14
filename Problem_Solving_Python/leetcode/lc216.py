# https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combination = []
        res = []

        def helper(start, depth, summ):
            if depth > k:
                return
            if summ == n and depth==k:
                res.append(combination[:])
                return

            for i in range(start, 9+1):
                combination.append(i)
                helper(i + 1, depth + 1, summ + i)
                combination.pop(-1)

        helper(1, 0, 0)
        return res