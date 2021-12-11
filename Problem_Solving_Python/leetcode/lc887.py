import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
def get_sol(): return Solution2()
class Solution:
    # tle
    def superEggDrop(self, k: int, n: int) -> int:
        @functools.lru_cache(None)
        def drop(floors_left, eggs):
            if floors_left==0: return 0
            if floors_left==1: return 1
            if eggs==1: # if we are left with only one egg, we need to check for each floor
                return floors_left
            minn = float('inf')
            for f in range(1, floors_left + 1):
                minn = min(minn, 1 + max(drop(f-1,eggs-1), drop(floors_left - f, eggs)))
            return minn

        return drop(n,k)
class Solution2:
    # https://leetcode.com/problems/super-egg-drop/discuss/158974/C%2B%2BJavaPython-2D-and-1D-DP-O(KlogN)
    def superEggDrop(self, k, n):
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for moves in range(1, n + 1):
            for eggs_left in range(1, k + 1):
                dp[moves][eggs_left] = dp[moves - 1][eggs_left - 1] + dp[moves - 1][eggs_left] + 1
            if dp[moves][k] >= n: return moves

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, get_sol().superEggDrop(k = 1, n = 2))
    def test2(self):
        self.assertEqual(3, get_sol().superEggDrop(k = 2, n = 6))
    def test3(self):
        self.assertEqual(4, get_sol().superEggDrop(k = 3, n = 14))
    def test4(self):
        self.assertEqual(16, get_sol().superEggDrop(k = 4,n = 2000))
    def test5(self):
        self.assertEqual(14, get_sol().superEggDrop(k = 100,n = 10000))
    # def test6(self):
    # def test7(self):
