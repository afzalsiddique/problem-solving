import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a,b):
            if a>b:
                return gcd(b,a)
            if a==0:
                return b
            return gcd(b%a,a)

        res=gcd(min(nums),max(nums))
        return res


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, get_sol().findGCD([2,5,6,9,10]))
    def test2(self):
        self.assertEqual(1, get_sol().findGCD([7,5,6,8,3]))
    def test3(self):
        self.assertEqual(3, get_sol().findGCD([3,3]))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):