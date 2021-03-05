# https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
import unittest
from typing import List


class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        res, comb = [], []

        def helper(start, depth, summ):
            if depth > k:
                return
            if summ == target and depth==k:
                res.append(comb[:])
                return

            for i in range(start, 9+1):
                comb.append(i)
                helper(i + 1, depth + 1, summ + i)
                comb.pop(-1)

        helper(1, 0, 0)
        return res

        # almost similar. same approch but with one less parameter
        res,comb = [],[]

        def helper(start, target):
            if len(comb)==k:
                if target!=0:
                    return
                else:
                    res.append(comb[:])
                    return

            for i in range(start,10):
                comb.append(i)
                helper(i+1, target-i)
                comb.pop(-1)

        helper(1,target)
        return res

class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = solution.combinationSum3(3, 7)
        expected = [[1,2,4]]
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        actual = solution.combinationSum3(3, 9)
        expected = [[1,2,6],[1,3,5],[2,3,4]]
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        actual = solution.combinationSum3(4, 1)
        expected = []
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        actual = solution.combinationSum3(3, 2)
        expected = []
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        actual = solution.combinationSum3(9, 45)
        expected = [[1,2,3,4,5,6,7,8,9]]
        self.assertEqual(expected, actual)