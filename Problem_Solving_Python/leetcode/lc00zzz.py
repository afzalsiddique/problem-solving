import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n=len(nums)
        prev_idx=-1
        neg=0
        maxx=0
        i=0
        while i<n:
            if nums[i]==0:
                prev_idx=i
                while nums[i]==0:
                    i+=1
                continue
            elif nums[i]<0:
                neg+=1
            if not neg&1:
                maxx=max(maxx,i-prev_idx)
            i+=1
        # neg=0
        # prev_idx=n
        # for i in reversed(range(n)):
        #     if nums[i]==0:
        #         prev_idx=i
        #     elif nums[i]<0:
        #         neg+=1
        #     if not neg&1:
        #         maxx=max(maxx,prev_idx-i)
        return maxx


class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums,k = [1,-1,-2,4,-7,3], 2
        Output= 7
        self.assertEqual(Output, get_sol().maxResult(nums,k))
    def test_2(self):
        nums,k = [10,-5,-2,4,0,3], 3
        Output= 17
        self.assertEqual(Output, get_sol().maxResult(nums,k))
    def test_3(self):
        nums,k = [1,-5,-20,4,-1,3,-6,-3], 2
        Output= 0
        self.assertEqual(Output, get_sol().maxResult(nums,k))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
