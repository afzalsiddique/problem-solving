import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def check(i):
            return sum(math.ceil(x/i) for x in quantities)<=n
        left,right=1,10**8
        while left<=right:
            mid = (left+right)//2
            if check(mid):
                right=mid-1
            else:
                left=mid+1
        return left

class MyTestCase(unittest.TestCase):
    def test1(self):
        n,quantities = 6,  [11,6]
        Output= 3
        self.assertEqual(Output, get_sol().minimizedMaximum(n,quantities))
    def test2(self):
        n,quantities = 7,  [15,10,10]
        Output= 5
        self.assertEqual(Output, get_sol().minimizedMaximum(n,quantities))
    def test3(self):
        n,quantities=1, [100000]
        Output= 100000
        self.assertEqual(Output, get_sol().minimizedMaximum(n,quantities))
    def test4(self):
        n,quantities= 2, [5,7]
        Output= 7
        self.assertEqual(Output, get_sol().minimizedMaximum(n,quantities))
    def test5(self):
        n,quantities= 22, [25,11,29,6,24,4,29,18,6,13,25,30]
        Output= 13
        self.assertEqual(Output, get_sol().minimizedMaximum(n,quantities))
    def test6(self):
        n,quantities= 1, [1]
        Output= 1
        self.assertEqual(Output, get_sol().minimizedMaximum(n,quantities))
    # def test7(self):
    # def test8(self):
