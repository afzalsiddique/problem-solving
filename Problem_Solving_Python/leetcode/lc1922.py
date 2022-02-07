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
    def test01(self):
        self.assertEqual(5, get_sol().countGoodNumbers(1))
    def test02(self):
        self.assertEqual(20, get_sol().countGoodNumbers(2))
    def test03(self):
        self.assertEqual(100, get_sol().countGoodNumbers(3))
    def test04(self):
        self.assertEqual(400, get_sol().countGoodNumbers(4))
    def test05(self):
        self.assertEqual(2000, get_sol().countGoodNumbers(5))
    def test06(self):
        self.assertEqual(564908303, get_sol().countGoodNumbers(50))
    def test07(self):
        self.assertEqual(643535977, get_sol().countGoodNumbers(806166225460393))
    def test08(self):
        self.assertEqual(8000, get_sol().countGoodNumbers(6))
    def test09(self):
        self.assertEqual(40000, get_sol().countGoodNumbers(7))
    def test10(self):
        self.assertEqual(160000, get_sol().countGoodNumbers(8))
    def test11(self):
        self.assertEqual(800000, get_sol().countGoodNumbers(9))
