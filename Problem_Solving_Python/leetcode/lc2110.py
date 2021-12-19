import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n=len(prices)
        i=1
        res=0
        while i<n:
            cnt=1
            while i<n and prices[i-1]-prices[i]==1:
                cnt+=1
                i+=1
            if cnt>1:
                res+= cnt*(cnt-1)//2
            i+=1
        return res + len(prices)


class Tester(unittest.TestCase):
    def test_1(self):
        self.assertEqual(7,get_sol().getDescentPeriods(prices = [3,2,1,4]))
    def test_2(self):
        self.assertEqual(16,get_sol().getDescentPeriods(prices = [3,2,1,8,7,6,5]))
    def test_3(self):
        self.assertEqual(4,get_sol().getDescentPeriods(prices = [8,6,7,7]))
    def test_4(self):
        self.assertEqual(1,get_sol().getDescentPeriods(prices = [1]))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
