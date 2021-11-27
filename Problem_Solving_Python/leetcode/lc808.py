import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    def soupServings(self, n: int) -> float:
        def func(a,b):
            if a<=0 and b<=0: return 0.5
            if a<=0: return 1.0
            if b<=0: return 0.0
            if (a,b) in dp: return dp[a,b]
            dp[a,b] = 0.25 * (func(a-100,b)+func(a-75,b-25)+func(a-50,b-50)+func(a-25,b-75))
            return dp[a,b]

        dp={}
        if n>50000: return 1.0
        return func(n,n)

class MyTestCase(unittest.TestCase):
    def test1(self):
        n = 50
        Output= 0.62500
        self.assertEqual(Output, get_sol().soupServings(n))
    def test2(self):
        n = 100
        Output= 0.71875
        self.assertEqual(Output, get_sol().soupServings(n))
    def test3(self):
        n = 660295675
        Output= 0.71875
        self.assertEqual(Output, get_sol().soupServings(n))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
