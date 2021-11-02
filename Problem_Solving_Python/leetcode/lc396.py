import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n=len(nums)
        count = Counter(nums)
        total = 0
        for i,num in enumerate(nums):
            total += i*num

        subtract=0
        for key in count:
            subtract+=key*count[key]

        maxx=total
        for num in nums:
            total-=subtract
            total+=num
            total+=num*(n-1)
            maxx=max(maxx,total)
        return maxx
class Solution2:
    # tle
    def maxRotateFunction(self, nums: List[int]) -> int:
        n=len(nums)
        count = Counter(nums)
        total = 0
        for i,num in enumerate(nums):
            total += i*num

        maxx=total
        for num in nums:
            count[num]-=1
            for key in count:
                total-=key*count[key]
            total+=num*(n-1)
            maxx=max(maxx,total)
            count[num]+=1
        return maxx

class MyTestCase(unittest.TestCase):
    def test1(self):
        nums = [4,3,2,6]
        Output= 26
        self.assertEqual(Output, get_sol().maxRotateFunction(nums))
    def test2(self):
        nums = [100]
        Output= 0
        self.assertEqual(Output, get_sol().maxRotateFunction(nums))
    def test3(self):
        nums = [4,3,3,6]
        Output= 27
        self.assertEqual(Output, get_sol().maxRotateFunction(nums))
    # def test4(self):
    # def test5(self):
    # def test6(self):
