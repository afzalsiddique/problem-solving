import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums,path):
            n=len(nums)
            if n==1:
                res.append(path+nums)
                return
            for i in range(n):
                if i>0 and nums[i]==nums[i-1]:continue
                temp = nums[:i]+nums[i+1:8]
                backtrack(temp, path+[nums[i]])

        res = []
        nums.sort()
        backtrack(nums,[])
        return res
class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        dp = {}

        def helper(nums):
            n = len(nums)
            if n == 1: return [nums]
            if tuple(nums) in dp: return dp[tuple(nums)]
            result = []
            for i in range(n):
                new_nums = nums[:i] + nums[i + 1:] # remove ith element
                ans = self.permuteUnique(new_nums)
                for item in ans:
                    if [nums[i]] + item not in result:
                        result.append([nums[i]] + item)
            dp[tuple(nums)] = result
            return result

        return helper(nums)
class Solution4:
    # bitmask+backtrack
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def turnOn(mask,i): return mask|(1<<i)
        def isOn(mask,i): return (mask>>i)&1
        def dfs(mask:int, path):
            if mask==GOAL:
                res.append(path)
                return
            vis=[False]*21
            for i in range(len(nums)):
                if isOn(mask,i): continue
                if vis[nums[i]+10]: continue # because -10<=nums[i]<=10
                vis[nums[i]+10]=True
                dfs(turnOn(mask,i), path + [nums[i]])
                # vis[nums[i]+10]=False # wrong

        GOAL=2**(len(nums))-1
        res = []
        nums.sort()
        dfs(0, [])
        return res
class Solution3:
    # bad solution because it uses set
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path:List[int]):
            if len(path)==n:
                res.add(tuple([nums[i] for i in path]))
                return
            for i in range(n):
                if i not in path:
                    backtrack(path[:]+[i])

        n=len(nums)
        res=set()
        backtrack([])
        return [list(x) for x in res]
class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([[1,1,2], [1,2,1], [2,1,1]], get_sol().permuteUnique([1,1,2]))
    def test2(self):
        self.assertEqual([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], get_sol().permuteUnique([1,2,3]))
    # def test3(self):
