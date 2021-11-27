import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def new21Game(self, n, k, w):
        if k==0: return 1.0
        if k-1+w<=n: return 1.0
        if k>n: return 0.0
        dp = [1.0] + [0.0] * n
        window_sum = 1.0
        for i in range(1, n + 1):
            dp[i] += window_sum / w
            if i < k:
                window_sum += dp[i]
            if i - w >= 0:
                window_sum -= dp[i - w]
        return sum(dp[k:])
class Solution2:
    # tle
    def new21Game(self, n: int, k: int, w: int) -> float:
        if k-1+w<=n: return 1.0
        if k>n: return 0.0
        p = 1 / w
        dp = [1.0]+[0.0]*n
        for i in range(1,n+1):
            for prev in range(max(0, i - w), min(i, k)):
                dp[i]+=dp[prev]*p

        return sum(dp[k:])

class MyTestCase(unittest.TestCase):
    def test1(self):
        n,k,maxPts = 10,  1,  10
        Output= 1.00000
        self.assertEqual(Output, get_sol().new21Game(n, k, maxPts))
    def test2(self):
        n,k,maxPts = 6,  1,  10
        Output= 0.60000
        self.assertEqual(Output, get_sol().new21Game(n, k, maxPts))
    def test3(self):
        n,k,maxPts = 21,  17,  10
        Output= 0.73278
        self.assertEqual(Output, get_sol().new21Game(n, k, maxPts))
    def test4(self):
        n,k,maxPts = 5710, 5070, 8516
        Output= 0.1364939468
        self.assertEqual(Output, get_sol().new21Game(n, k, maxPts))
    def test5(self):
        n,k,maxPts = 1, 0, 3
        Output= 1.0
        self.assertEqual(Output, get_sol().new21Game(n, k, maxPts))
    # def test6(self):
    # def test7(self):
