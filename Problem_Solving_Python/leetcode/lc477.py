import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n=len(nums)
        total = 0
        for j in range(32):
            cnt=0
            for num in nums:
                cnt+= (num>>j)&1
            total+= (cnt*(n-cnt))
        return total

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(6, get_sol().totalHammingDistance([4,14,2]))
    def test02(self):
        self.assertEqual(4, get_sol().totalHammingDistance([4,14,4]))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
