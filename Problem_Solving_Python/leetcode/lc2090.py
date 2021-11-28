import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        res=[-1]*n
        pre=[0]+list(itertools.accumulate(nums))
        for i in range(k,n-k):
            res[i]=(pre[i+k+1]-pre[i-k])//(2*k+1)
        return res


class MyTestCase(unittest.TestCase):
    def test1(self):
        nums,k = [7,4,3,9,1,8,5,2,6],  3
        Output= [-1,-1,-1,5,4,4,-1,-1,-1]
        self.assertEqual(Output, get_sol().getAverages(nums,k))
    def test2(self):
        nums,k = [100000],  0
        Output= [100000]
        self.assertEqual(Output, get_sol().getAverages(nums,k))
    def test3(self):
        nums,k = [8],  100000
        Output= [-1]
        self.assertEqual(Output, get_sol().getAverages(nums,k))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
