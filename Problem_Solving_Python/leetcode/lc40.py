# https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
# https://leetcode.com/problems/combination-sum-ii/discuss/16878/Combination-Sum-I-II-and-III-Java-solution-(see-the-similarities-yourself)
import unittest
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                combination.append(candidates[i])
                helper(i + 1, summ + candidates[i])
                combination.pop(-1)

        helper(0,0)
        return li

class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = sorted(solution.combinationSum2([10,1,2,7,6,1,5], 8))
        expected = sorted([
                            [1,1,6],
                            [1,2,5],
                            [1,7],
                            [2,6]
                            ])
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        actual = sorted(solution.combinationSum2([2,5,2,1,2], 5))
        expected = sorted([
                            [1,2,2],
                            [5]
                            ])
        self.assertEqual(expected, actual)