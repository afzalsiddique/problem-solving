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
        Output= 7
        self.assertEqual(Output, get_sol().minDifficulty(li= [6, 5, 4, 3, 2, 1], d = 2))
    def test2(self):
        Output= -1
        self.assertEqual(Output, get_sol().minDifficulty(li= [9, 9, 9], d = 4))
    def test3(self):
        Output= 3
        self.assertEqual(Output, get_sol().minDifficulty(li= [1, 1, 1], d = 3))
    def test4(self):
        Output= 15
        self.assertEqual(Output, get_sol().minDifficulty(li= [7, 1, 7, 1, 7, 1], d = 3))
    def test5(self):
        Output= 843
        self.assertEqual(Output, get_sol().minDifficulty(li= [11, 111, 22, 222, 33, 333, 44, 444], d = 6))
    # def test5(self):
    # def test6(self):