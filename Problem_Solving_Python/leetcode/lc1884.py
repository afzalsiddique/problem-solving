import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def twoEggDrop(self, n: int) -> int:
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
        return drop(n,2)
class Solution2:
    # https://www.youtube.com/watch?v=uBhSIKLlvdk
    def twoEggDrop(self, n: int) -> int:
        #    x+(x-1)+(x-2)+(x-3)+...+1 <= n
        # => x**2 + x -2n = 0
        # x1 = (-b+sqrt(b**2-4*a*c))/2
        # x2 = (-b-sqrt(b**2-4*a*c))/2
        x1 = (-1 + math.sqrt(1+8*n))/2
        x2 = (-1 - math.sqrt(1+8*n))/2
        # return the positive root
        if x1>0: return math.ceil(x1)
        return math.ceil(x2)

class MyTestCase(unittest.TestCase):
    def test1(self):
        n=2
        Output = 2
        self.assertEqual(Output, get_sol().twoEggDrop(n))
    def test2(self):
        n=100
        Output = 14
        self.assertEqual(Output, get_sol().twoEggDrop(n))
    def test3(self):
        n=835
        Output = 41
        self.assertEqual(Output, get_sol().twoEggDrop(n))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
