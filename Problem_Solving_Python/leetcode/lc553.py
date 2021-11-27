import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums)==1: return str(nums[0])
        if len(nums)==2: return str(nums[0]) + '/' + str(nums[1])
        numerator = nums[0]
        den = [str(x) for x in nums[1:]]
        den = '('+'/'.join(den)+')'
        return str(numerator) + '/' + den

class MyTestCase(unittest.TestCase):
    def test1(self):
        nums = [1000,100,10,2]
        Output= "1000/(100/10/2)"
        self.assertEqual(Output, get_sol().optimalDivision(nums))
    def test2(self):
        nums = [2,3,4]
        Output= "2/(3/4)"
        self.assertEqual(Output, get_sol().optimalDivision(nums))
    def test3(self):
        nums = [2]
        Output= "2"
        self.assertEqual(Output, get_sol().optimalDivision(nums))
    def test4(self):
        nums = [3,2]
        Output= "3/2"
        self.assertEqual(Output, get_sol().optimalDivision(nums))
    # def test5(self):
    # def test6(self):
    # def test7(self):
