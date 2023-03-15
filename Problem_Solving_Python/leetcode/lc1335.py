import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
def get_sol(): return Solution()
# Rephrase the question:
# Given an array, cut it into d contiguous subarrays and return the minimum sum of max of each subarray
class Solution:
    def minDifficulty(self, li: List[int], d: int) -> int:
        @functools.lru_cache(None)
        def dfs(i,left):
            if left<0: return float('inf')
            if i==n and left==0: return 0
            res=float('inf')
            max_d=float('-inf')
            for j in range(i,n):
                max_d=max(max_d, li[j]) # record max distance within [i,j]
                res=min(res,max_d+dfs(j+1,left-1))
            return res

        n=len(li)
        res=dfs(0,d)
        return res if res!=float('inf') else -1
class Solution2:
    # bad solution
    def minDifficulty(self, li: List[int], d: int) -> int:
        @functools.lru_cache(None)
        def dfs(i,left):
            if left<0: return float('inf')
            if i==n and left==0: return 0
            res=float('inf')
            for j in range(i,n):
                max_d=max(li[i:j + 1]) # not good. update requires O(n) time
                res=min(res,max_d+dfs(j+1,left-1))
            return res

        n=len(li)
        res=dfs(0,d)
        return res if res!=float('inf') else -1

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(7, get_sol().minDifficulty([6, 5, 4, 3, 2, 1], 2))
    def test2(self):
        self.assertEqual(1, get_sol().minDifficulty([9, 9, 9], 4))
    def test3(self):
        self.assertEqual(3, get_sol().minDifficulty([1, 1, 1], 3))
    def test4(self):
        self.assertEqual(15, get_sol().minDifficulty([7, 1, 7, 1, 7, 1], 3))
    def test5(self):
        self.assertEqual(843, get_sol().minDifficulty([11, 111, 22, 222, 33, 333, 44, 444], 6))
    # def test5(self):
    # def test6(self):