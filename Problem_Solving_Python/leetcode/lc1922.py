import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9+7
        def calculate_power(x,n): # (x to the power n) % MOD
            if n==0: return 1
            if n%2==0:
                tmp = calculate_power(x,n//2)
                return ((tmp%MOD)*(tmp%MOD))%MOD
            else:
                tmp = calculate_power(x,n-1)
                return ((x%MOD)*(tmp%MOD)) % MOD

        if n&1:
            ans1 = calculate_power(5,n//2+1)
            ans2 = calculate_power(4,n//2)
        else:
            ans1 = calculate_power(5,n//2)
            ans2 = calculate_power(4,n//2)
        return ((ans1%MOD)*(ans2%MOD))%MOD


class MyTestCase(unittest.TestCase):
    def test1(self):
        n = 1
        Output= 5
        self.assertEqual(Output, get_sol().countGoodNumbers(n))
    def test2(self):
        n = 2
        Output= 20
        self.assertEqual(Output, get_sol().countGoodNumbers(n))
    def test3(self):
        n = 3
        Output= 100
        self.assertEqual(Output, get_sol().countGoodNumbers(n))
    def test4(self):
        n = 4
        Output= 400
        self.assertEqual(Output, get_sol().countGoodNumbers(n))
    def test5(self):
        n = 5
        Output= 2000
        self.assertEqual(Output, get_sol().countGoodNumbers(n))
    def test6(self):
        n = 806166225460393
        Output= 643535977
        self.assertEqual(Output, get_sol().countGoodNumbers(n))
    # def test7(self):
    # def test8(self):
