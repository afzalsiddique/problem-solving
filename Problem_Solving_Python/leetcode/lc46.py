import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
# https://leetcode.com/problems/permutations/discuss/18462/Share-my-three-different-solutions
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

class Solution3:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path:List[int]):
            if len(path)==n:
                res.append(path)
                return
            for x in nums:
                if x not in path:
                    backtrack(path[:]+[x])

        n=len(nums)
        res=[]
        backtrack([])
        return res

class Tester(unittest.TestCase):
    def test_1(self):
        self.assertEqual([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], get_sol().permute([1,2,3]))
    def test_2(self):
        self.assertEqual([[0,1],[1,0]], get_sol().permute([0,1]))
    def test_3(self):
        self.assertEqual([[1]], get_sol().permute([1]))