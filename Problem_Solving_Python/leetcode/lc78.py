# https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
# https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)/26331
import unittest
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n, res, comb = len(nums), [], []

        def backtrack(start):
            res.append(comb[:])
            for i in range(start, n):
                comb.append(nums[i])
                backtrack(i+1)
                comb.pop(-1)

        backtrack(0)
        return res

class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = sorted(solution.subsets([1,2,3]))
        expected = sorted([[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        actual = sorted(solution.subsets([0]))
        expected = sorted([[],[0]])
        self.assertEqual(expected, actual)