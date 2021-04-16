import unittest
from typing import List


class Solution:
    def permute(self, nums):
        # backtracking 1
        res, path = [], []

        def dfs(nums):
            if not nums:
                res.append(path[:])
            for i in range(len(nums)):
                path.append(nums[i])
                dfs(nums[:i] + nums[i + 1:])
                path.pop(-1)

        dfs(nums)
        return res

        # backtracking 2
        res = []

        def dfs(nums, path):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]])

        dfs(nums, [])
        return res

# https://leetcode.com/problems/permutations/discuss/18462/Share-my-three-different-solutions

class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        self.assertEqual(expected, solution.permute([1,2,3]))

    def test_2(self):
        solution = Solution()
        expected = [[0,1],[1,0]]
        self.assertEqual(expected, solution.permute([0,1]))

    def test_3(self):
        solution = Solution()
        self.assertEqual([[1]], solution.permute([1]))