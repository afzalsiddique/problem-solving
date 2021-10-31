import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        n=len(nums)
        x=start
        res = 0
        vis=set()
        q=deque([x])
        while q:
            for _ in range(len(q)):
                x = q.popleft()
                if x in vis: continue
                if x==goal: return res
                vis.add(x)
                for i in range(n):
                    if x+nums[i]==goal: return res+1
                    if x-nums[i]==goal: return res+1
                    if x^nums[i]==goal: return res+1
                    if 0<=x+nums[i]<=1000: q.append(x+nums[i])
                    if 0<=x-nums[i]<=1000: q.append(x-nums[i])
                    if 0<=x^nums[i]<=1000: q.append(x^nums[i])
            res+=1
        return -1

class MyTestCase(unittest.TestCase):
    def test1(self):
        nums,start,goal = [1,3],  6,  4
        Output= 2
        self.assertEqual(Output, get_sol().minimumOperations(nums,start,goal))
    def test2(self):
        nums,start,goal = [2,4,12],  2,  12
        Output= 2
        self.assertEqual(Output, get_sol().minimumOperations(nums,start,goal))
    def test3(self):
        nums,start,goal = [3,5,7],  0,  -4
        Output= 2
        self.assertEqual(Output, get_sol().minimumOperations(nums,start,goal))
    def test4(self):
        nums,start,goal = [2,8,16],  0,  1
        Output= -1
        self.assertEqual(Output, get_sol().minimumOperations(nums,start,goal))
    def test5(self):
        nums,start,goal = [1],  0,  3
        Output= 3
        self.assertEqual(Output, get_sol().minimumOperations(nums,start,goal))
    # def test6(self):
