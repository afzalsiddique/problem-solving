import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def sum_range(lo, hi): # both inclusive
            if lo>hi: return 0
            if lo<=0: lo=1
            return hi * (hi + 1) // 2 - (lo - 1) * lo // 2
        def valid(mid):
            hi=mid-1
            lo = mid-items_on_the_left
            sum_left = sum_range(lo,hi)

            hi=mid-1
            lo=mid-items_on_the_right
            sum_right=sum_range(lo,hi)

            minn= sum_left+mid+sum_right
            return minn<=maxSum

        maxSum-=n # subtract 1 from every item in the array. the condition becomes A[i]>=0
        if maxSum==0: return 1
        items_on_the_right=n-index-1
        items_on_the_left = index
        left=0
        right=maxSum+1
        while left<=right:
            mid = (left+right)//2
            if valid(mid-1): # subtract 1 from every item in the array. the condition becomes A[i]>=0
                left=mid+1
            else:
                right=mid-1
        return left-1


class MyTestCase(unittest.TestCase):
    def test1(self):
        n,index,maxSum = 4,  2,   6
        Output= 2
        self.assertEqual(Output, get_sol().maxValue(n,index,maxSum))
    def test2(self):
        n,index,maxSum = 6,  1,   10
        Output= 3
        self.assertEqual(Output, get_sol().maxValue(n,index,maxSum))
    def test3(self):
        n,index,maxSum = 8,  2,   100
        Output= 14
        self.assertEqual(Output, get_sol().maxValue(n,index,maxSum))
    def test4(self):
        n,index,maxSum = 8, 7, 14
        Output= 4
        self.assertEqual(Output, get_sol().maxValue(n,index,maxSum))
    def test5(self):
        n,index,maxSum = 4, 0, 4
        Output= 1
        self.assertEqual(Output, get_sol().maxValue(n,index,maxSum))
    def test6(self):
        n,index,maxSum = 9, 1, 9
        Output= 1
        self.assertEqual(Output, get_sol().maxValue(n,index,maxSum))