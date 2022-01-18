from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import cache; from heapq import *; import unittest; from typing import List, Optional; import functools;from sortedcontainers import SortedList
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/discuss/1239980/Python-7-lines-dp-%2B-2liner-explained
    # dp[index][curTimeCost]=skipCount. not ideal. Because the range for curTimeCost is very large and it is float
    # instead use dp[index][skipCount]=minTimeCost
    def minSkips(self, A: List[int], s: int, h: int) -> int:
        EP=1e-9 # 10/3 = 3.33333333335. subtract a small number to compensate for this kind of inaccuracy
        @cache
        def dfs(i,skip): # skip-> If we use at most 'skip' rest, then calculate the minimum time to reach.
            if skip<0: # We skipped more rests than available
                return float('inf')
            if i==n:
                return 0

            res=min(A[i]/s+dfs(i+1,skip-1),ceil(A[i]/s+dfs(i+1,skip)-EP))
            return res

        n=len(A)
        for skip in range(0,n+1):
            if dfs(0,skip)<=h: # Check if we can reach if we skip at most 'skip' rests
                return skip
        return -1
class Solution2:
    # wrong. dp[index][curTimeCost]=skipCount
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        def isWhole(x:float): return x==int(x)
        def recurse(i,hours):
            if i==n:
                if hours>=0.0:
                    return 0
                return float('inf')

            res=float('inf')
            if isWhole(hours):
                res=min(res,recurse(i+1,floor(hours)-dist[i]/speed))
            else:
                res=min(res,recurse(i+1,floor(hours)-dist[i]/speed))
                res=min(res, 1+recurse(i+1,hours-dist[i]/speed))
            return res


        n=len(dist)
        res= recurse(0,hoursBefore)
        return res if res!=float('inf') else -1
class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(1,get_sol().minSkips([1,3,2], 4,2))
    def test02(self):
        self.assertEqual(2,get_sol().minSkips([7,3,5,5], 2, 10))
    def test03(self):
        self.assertEqual(-1,get_sol().minSkips([7,3,5,5], 1, 10))
    def test04(self):
        self.assertEqual(7,get_sol().minSkips([2,1,5,4,4,3,2,9,2,10], 6, 7))
    def test05(self):
        self.assertEqual(-1,get_sol().minSkips([18,66,64,12,97,7,15,20,81,21,88,55,77,9,50,49,77,60,68,33,71,2,88,93,15,88,69,97,35,99,83,44,15,38,56,21,59,1,93,93,34,65,98,23,65,14,81,39,82,65,78,26,20,48,98,21,70,100,68,1,77,42,63,3], 17, 160))

# [2,1,5,4,4,3,2,9,2,10]
