import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/super-pow/discuss/84472/C%2B%2B-Clean-and-Short-Solution
    def superPow(self, a: int, b: List[int]) -> int:
        def pow_mod(a,b): # (a**b)%k
            res = 1
            for i in range(b):
                res *= a%k
                res %= k
            return res
        def f(a: int, b: List[int]) -> int:
            if not b: return 1
            last_digit = b.pop()
            return pow_mod(f(a,b),10) * pow_mod(a,last_digit) % k

        k=1337
        return f(a,b)



class MyTestCase(unittest.TestCase):
    def test1(self):
        a,b = 2,  [3]
        Output= 8
        self.assertEqual(Output, get_sol().superPow(a,b))
    def test2(self):
        a,b = 2,  [1,0]
        Output= 1024
        self.assertEqual(Output, get_sol().superPow(a,b))
    def test3(self):
        a,b = 1,  [4,3,3,8,5,2]
        Output= 1
        self.assertEqual(Output, get_sol().superPow(a,b))
    def test4(self):
        a,b = 2147483647,  [2,0,0]
        Output= 1198
        self.assertEqual(Output, get_sol().superPow(a,b))
    def test5(self):
        a,b = 2147483647,  [2,3,5]
        Output= 1184
        self.assertEqual(Output, get_sol().superPow(a,b))
    def test6(self):
        a,b = 2,  [1,8]
        Output= 92
        self.assertEqual(Output, get_sol().superPow(a,b))
