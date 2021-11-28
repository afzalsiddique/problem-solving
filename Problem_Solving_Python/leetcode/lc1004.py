import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l,r=0,0
        odd_cnt=0
        res=float('-inf')
        while r<n:
            if nums[r]==0: odd_cnt+=1
            r+=1
            while odd_cnt>k:
                if nums[l]==0: odd_cnt-=1
                l+=1
            res=max(res,r-l)

        return res


class MyTestCase(unittest.TestCase):
    def test_01(self):
        nums,k = [1,1,1,0,0,0,1,1,1,1,0],2
        Output= 6
        self.assertEqual(Output, get_sol().longestOnes(nums,k))
    def test_02(self):
        nums,k = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3
        Output= 10
        self.assertEqual(Output, get_sol().longestOnes(nums,k))
