import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution2()
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        di=defaultdict(int)
        di[0]=-1 # first occurence of 0 is at index -1
        cur=0
        for i,x in enumerate(nums):
            cur+=x
            y=cur%k
            if y in di and i-di[y]>=2:
                return True
            if y not in di:
                di[y]=i
        return False
class Solution2:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        di=defaultdict(int)
        di[0]=-1 # first occurence of 0 is at index -1
        cur=0
        for i,x in enumerate(nums):
            cur=(cur+x)%k
            if cur in di and i-di[cur]>=2:
                return True
            if cur not in di:
                di[cur]=i
        return False

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(True, get_sol().checkSubarraySum([23,2,4,6,7],  6))
    def test02(self):
        self.assertEqual(True, get_sol().checkSubarraySum([23,2,6,4,7],  6))
    def test03(self):
        self.assertEqual(False, get_sol().checkSubarraySum([23,2,6,4,7],  13))
    def test04(self):
        self.assertEqual(True, get_sol().checkSubarraySum([23,2,4,6,6], 7))
    def test05(self):
        self.assertEqual(False, get_sol().checkSubarraySum([0], 1))
    def test06(self):
        self.assertEqual(True, get_sol().checkSubarraySum([5,0,0,0], 3))
    def test07(self):
        self.assertEqual(True, get_sol().checkSubarraySum([0,0], 1))
    def test08(self):
        self.assertEqual(False, get_sol().checkSubarraySum([1,0], 2))
    def test09(self):
        self.assertEqual(True, get_sol().checkSubarraySum([7,0], 7))
    def test10(self):
        self.assertEqual(False, get_sol().checkSubarraySum([7], 7))
    def test11(self):
        self.assertEqual(False, get_sol().checkSubarraySum([1,2,0], 6))
    def test12(self):
        self.assertEqual(True, get_sol().checkSubarraySum([2,4,3], 6))
    def test13(self):
        self.assertEqual(True, get_sol().checkSubarraySum([1,1], 1))
    def test14(self):
        self.assertEqual(False, get_sol().checkSubarraySum([1,0,1,0,1], 4))
    def test15(self):
        self.assertEqual(False, get_sol().checkSubarraySum([5,2,0,2,5], 6))
    def test16(self):
        self.assertEqual(True, get_sol().checkSubarraySum([1,2,3], 5))
