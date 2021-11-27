import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    def medianSlidingWindow(self,nums, k):
        def move(h1, h2):
            x, i = heappop(h1)
            heappush(h2, (-x, i))
        def get_med(h1, h2, k):
            return h2[0][0] * 1.0 if k & 1 else (h2[0][0]-h1[0][0]) / 2.0

        if k==1: return nums
        left, right = [], [] # right contains one more numbers if k is odd
        for idx, a in enumerate(nums[:k]):
            heappush(left, (-a,idx))
        for _ in range(math.ceil(k/2)):
            move(left, right)
        ans = [get_med(left, right, k)]
        for i in range(k,len(nums)):
            x=nums[i]
            if x >= right[0][0]:
                heappush(right, (x, i))
                if nums[i-k] <= (left[0][0]*(-1)):# nums[i-k] is expiring. expiring num is in the left side. So add another num from the right to the left
                    move(right, left)
            else:
                heappush(left, (-x, i))
                if nums[i-k] >= (right[0][0]): # expiring num is in the right side. So add another num from the left to the right
                    move(left, right)
            while left and left[0][1] <= i-k:
                heappop(left)
            while right and right[0][1] <= i-k:
                heappop(right)
            ans.append(get_med(left, right, k))
        return ans



class MyTestCase(unittest.TestCase):
    def test1(self):
        nums, k = [1,3,-1,-3,5,3,6,7],3
        Output= [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
        self.assertEqual(Output, get_sol().medianSlidingWindow(nums,k))
    def test2(self):
        nums, k = [1,2,3,4,2,3,1,4,2], 3
        Output= [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
        self.assertEqual(Output, get_sol().medianSlidingWindow(nums,k))
    def test3(self):
        nums, k = [1,2], 1
        Output= [1.00000,2.00000]
        self.assertEqual(Output, get_sol().medianSlidingWindow(nums,k))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
