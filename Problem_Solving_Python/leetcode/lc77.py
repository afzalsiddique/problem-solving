# https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        combination = []
        def backtrack(start, depth):
            if depth > k:
                return
            if depth == k:
                ret.append(combination[:])
                return

            for i in range(start, n+1):
                combination.append(i)
                backtrack(i+1, depth+1)
                combination.pop(-1)

        backtrack(1, 0)
        return ret