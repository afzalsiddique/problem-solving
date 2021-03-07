# https://leetcode.com/problems/subsets-ii/
import unittest
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n, res = len(nums),[]

        def dfs(start, path):
            res.append(path)

            for i in range(start, n):
                if i>start and nums[i]==nums[i-1]:continue
                dfs(i+1, path+[nums[i]])

        nums.sort()
        dfs(0,[])
        return res
        # similar but with one less parameter
        n, res, comb = len(nums), [], []

        def backtrack(start):
            res.append(comb[:])
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                comb.append(nums[i])
                backtrack(i + 1)
                comb.pop(-1)

        nums.sort() # if not sorted duplicates will not be together
        backtrack(0)
        return res


class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = sorted(solution.subsetsWithDup([1, 2, 2]))
        expected = sorted([
            [2],
            [1],
            [1, 2, 2],
            [2, 2],
            [1, 2],
            []
        ])
        self.assertEqual(expected, actual)
