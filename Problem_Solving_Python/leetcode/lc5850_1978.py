from itertools import accumulate; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=max(nums)
        b=min(nums)
        def gcd(a,b):
            if b>a: return gcd(b,a)
            if b==0: return a
            return gcd(a%b,b)
        return gcd(a,b)

class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [2,5,6,9,10]
        Output= 2
        self.assertEqual(Output, get_sol().findGCD(nums))
    def test_2(self):
        nums = [7,5,6,8,3]
        Output= 1
        self.assertEqual(Output, get_sol().findGCD(nums))
    def test_3(self):
        nums = [3,3]
        Output= 3
        self.assertEqual(Output, get_sol().findGCD(nums))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):