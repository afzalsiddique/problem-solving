import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)
        peak=True
        i=0
        cur=0
        maxx=float('-inf')
        while i<n:
            if peak:
                while i+1<n and nums[i]<=nums[i+1]:
                    i+=1
                cur+=nums[i]
                maxx=max(maxx,cur)
            else:
                while i+1<n and nums[i]>=nums[i+1]:
                    i+=1
                cur-=nums[i]
            peak = not peak
            i+=1
        return maxx



class MyTestCase(unittest.TestCase):
    def test1(self):
        nums = [4,2,5,3]
        Output= 7
        self.assertEqual(Output, get_sol().maxAlternatingSum(nums))
    def test2(self):
        nums = [5,6,7,8]
        Output= 8
        self.assertEqual(Output, get_sol().maxAlternatingSum(nums))
    def test3(self):
        nums = [6,2,1,2,4,5]
        Output= 10
        self.assertEqual(Output, get_sol().maxAlternatingSum(nums))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
