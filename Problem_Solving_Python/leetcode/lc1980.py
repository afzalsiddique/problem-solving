import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        sett = set()
        n=len(nums)
        for x in nums:
            sett.add(int(x,2))
        for i in range(0,2**n):
            if i not in sett:
                ans = bin(i)[2:]
                return '0'*(n-len(ans)) + ans

class MyTestCase(unittest.TestCase):
    def test1(self):
        nums = ["111","011","001"]
        Output= "101"
        self.assertEqual(Output, get_sol().findDifferentBinaryString(nums))
    def test2(self):
        nums = ["01","10"]
        Output= "11"
        self.assertEqual(Output, get_sol().findDifferentBinaryString(nums))
    def test3(self):
        nums = ["00","01"]
        Output= "11"
        self.assertEqual(Output, get_sol().findDifferentBinaryString(nums))
    def test4(self):
        nums = ["1"]
        Output= "0"
        self.assertEqual(Output, get_sol().findDifferentBinaryString(nums))
    def test5(self):
        nums = ["10","11"]
        Output= "00"
        self.assertEqual(Output, get_sol().findDifferentBinaryString(nums))
