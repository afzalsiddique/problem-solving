import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # tle
    def superEggDrop(self, k: int, n: int) -> int:
        def drop(floors_left, eggs):
            if floors_left<=1:
                return floors_left
            if eggs==1: # if we are left with only one egg, we need to check for each floor
                return floors_left
            if (floors_left, eggs) in dp: return dp[floors_left, eggs]
            minn = float('inf')
            for f in range(1, floors_left + 1):
                minn = min(minn, 1 + max(drop(f-1,eggs-1), drop(floors_left - f, eggs)))
            dp[floors_left, eggs]=minn
            return minn

        dp = {}
        return drop(n,k)

class MyTestCase(unittest.TestCase):
    def test1(self):
        k,n = 1,  2
        Output= 2
        self.assertEqual(Output, get_sol().superEggDrop(k,n))
    def test2(self):
        k,n = 2,  6
        Output= 3
        self.assertEqual(Output, get_sol().superEggDrop(k,n))
    def test3(self):
        k,n = 3,  14
        Output= 4
        self.assertEqual(Output, get_sol().superEggDrop(k,n))
    def test4(self):
        k,n = 4, 2000
        Output= 4
        self.assertEqual(Output, get_sol().superEggDrop(k,n))
    # def test5(self):
    # def test6(self):
    # def test7(self):
