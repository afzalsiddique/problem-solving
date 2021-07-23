import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        pow=[]
        ENOUGH = 20
        MOD = 10**9+7
        def create_power_table():
            x=1
            for _ in range(ENOUGH):
                pow.append(x)
                x*=2
        if n==1: return 1
        create_power_table()
        x=1
        for i in range(2,n+1): # n inclusive
            l = len(bin(i))-2
            x *= pow[l]
            x += i
            x %= MOD # should be inside for loop.
        return x

class MyTestCase(unittest.TestCase):
    def test_1(self):
        n = 1
        Output= 1
        self.assertEqual(Output, get_sol().concatenatedBinary(n))
    def test_2(self):
        n = 2
        Output= 6
        self.assertEqual(Output, get_sol().concatenatedBinary(n))
    def test_3(self):
        n = 3
        Output= 27
        self.assertEqual(Output, get_sol().concatenatedBinary(n))
    def test_4(self):
        n = 12
        Output= 505379714
        self.assertEqual(Output, get_sol().concatenatedBinary(n))
    def test_5(self):
        n=63556
        Output = 846105501
        self.assertEqual(Output, get_sol().concatenatedBinary(n))
    def test_6(self):
        n=100000
        Output = 757631812
        self.assertEqual(Output, get_sol().concatenatedBinary(n))
    # def test_7(self):
    # def test_8(self):
