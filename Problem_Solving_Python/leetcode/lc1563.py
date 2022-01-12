import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # tle
    def stoneGameV(self, stoneValue: List[int]) -> int:
        @functools.lru_cache(None)
        def dfs(l:int,r:int): # both inclusive
            if r-l+1==1:
                return 0
            if r-l+1==2:
                return min(stoneValue[l],stoneValue[r])

            res=float('-inf')
            # left: [l, i], right: [i + 1, r]
            for i in range(l,r):
                left=prefix[i+1]-prefix[l]
                right=prefix[r+1]-prefix[i+1]
                if right<left: # right partition gives less score. work on right partition
                    res=max(res,right+dfs(i+1,r))
                elif left<right:
                    res=max(res,left+dfs(l,i))
                else:
                    res=max(res,left+dfs(i+1,r),left+(dfs(l,i)))
            return res

        prefix=[0]+list(itertools.accumulate(stoneValue))
        return dfs(0,len(stoneValue)-1)

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(10, get_sol().stoneGameV([6,2,5,5]))
    def test02(self):
        self.assertEqual(18, get_sol().stoneGameV([6,2,3,4,5,5]))
    def test03(self):
        self.assertEqual(28, get_sol().stoneGameV([7,7,7,7,7,7,7]))
    def test04(self):
        self.assertEqual(0, get_sol().stoneGameV([4]))
    def test05(self):
        self.assertEqual(0, get_sol().stoneGameV([39994,3,4,10000,10000,10000,10000,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1000000]))
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
