import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
# similar to leetcode 47
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        INVALID=-1
        def check(x,y):
            tmp = math.sqrt(x+y)
            return math.floor(tmp)==math.ceil(tmp)
        def backtrack(nums:List[int],last:int):
            if not nums: return 1

            res=0
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]: continue
                cur=nums[i]
                if last==INVALID:
                    res+=backtrack(nums[:i]+nums[i+1:],cur)
                else:
                    if check(last,cur):
                        res+=backtrack(nums[:i]+nums[i+1:],cur)
            return res

        nums.sort()
        return backtrack(nums,INVALID)
class Solution2:
    # tle
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def backtrack(nums:List[int],path:List[int]):
            if not nums:
                for x,y in zip(path,path[1:]):
                    tmp=math.sqrt(x+y)
                    if math.floor(tmp)!=math.ceil(tmp):
                        return 0
                return 1

            res=0
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]: continue
                res+=backtrack(nums[:i]+nums[i+1:],path[:]+[nums[i]])
            return res

        nums.sort()
        return backtrack(nums,[])



class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, get_sol().numSquarefulPerms( [1,17,8]))
    def test2(self):
        self.assertEqual(1, get_sol().numSquarefulPerms( [2,2,2]))
    def test3(self):
        self.assertEqual(1, get_sol().numSquarefulPerms( [89,72,71,44,50,72,26,79,33,27,84]))