from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# https://leetcode.com/problems/permutations/discuss/18462/Share-my-three-different-solutions
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def turnOn(mask,i): return mask|(1<<i)
        def isOn(mask,i): return (mask>>i)&1
        GOAL=2**(len(nums))-1
        def backtrack(mask,path):
            if mask==GOAL:
                res.append(path)
                return
            for i in range(len(nums)):
                if not isOn(mask,i):
                    backtrack(turnOn(mask,i),path+[nums[i]])

        res=[]
        backtrack(0,[])
        return res
class Solution4:
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


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], get_sol().permute([1,2,3]))
    def test02(self):
        self.assertEqual([[0,1],[1,0]], get_sol().permute([0,1]))
    def test03(self):
        self.assertEqual([[1]], get_sol().permute([1]))