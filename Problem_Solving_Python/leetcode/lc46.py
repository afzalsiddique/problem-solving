import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # backtracking 1
    def permute(self, nums):
        res = []
        def dfs(nums, path):
            if not nums: res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]])

        dfs(nums, [])
        return res

class Solution2:
    # backtracking 2
    def permute(self, nums):
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

# https://leetcode.com/problems/permutations/discuss/18462/Share-my-three-different-solutions

class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = get_sol()
        expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        self.assertEqual(expected, solution.permute([1,2,3]))

    def test_2(self):
        solution = Solution()
        expected = [[0,1],[1,0]]
        self.assertEqual(expected, solution.permute([0,1]))

    def test_3(self):
        solution = Solution()
        self.assertEqual([[1]], solution.permute([1]))