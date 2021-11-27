import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        return 0
class Solution2:
    # https://leetcode.com/problems/count-of-range-sum/discuss/407655/Python-different-concise-solutions
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        return 0

class MyTestCase(unittest.TestCase):
    def test1(self):
        nums,lower,upper = [-2,5,-1],  -2,  2
        Output= 3
        self.assertEqual(Output, get_sol().countRangeSum(nums,lower,upper))
    def test2(self):
        nums,lower,upper = [0],  0,  0
        Output= 1
        self.assertEqual(Output, get_sol().countRangeSum(nums,lower,upper))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
