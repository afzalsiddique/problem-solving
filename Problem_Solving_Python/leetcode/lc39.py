# https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
import unittest
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


class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = sorted(solution.combinationSum([2,3,6,7], 7))
        expected = sorted([[2,2,3],[7]])
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        actual = sorted(solution.combinationSum([2,3,5], 8))
        expected = sorted([[2,2,2,2],[2,3,3],[3,5]])
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        actual = sorted(solution.combinationSum([2], 1))
        expected = sorted([])
        self.assertEqual(expected, actual)

    def test_4  (self):
        solution = Solution()
        actual = sorted(solution.combinationSum([1], 1))
        expected = sorted([[1]])
        self.assertEqual(expected, actual)