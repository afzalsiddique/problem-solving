import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n=len(nums)
        left = [False]*n
        right = [False]*n
        cur_max = nums[0]
        for i in range(1,n-1):
            if cur_max<nums[i]:
                left[i]=True
            cur_max=max(cur_max,nums[i])

        cur_min=nums[-1]
        for i in range(n-1,0,-1):
            if cur_min>nums[i]:
                right[i]=True
            cur_min = min(cur_min, nums[i])

        res = 0
        for i in range(1,n-1):
            if left[i] and right[i]:
                res+=2
            elif nums[i-1]<nums[i]<nums[i+1]:
                res+=1
        return res


class MyTestCase(unittest.TestCase):
    def test1(self):
        nums = [1,2,3]
        Output= 2
        self.assertEqual(Output, get_sol().sumOfBeauties(nums))
    def test2(self):
        nums = [2,4,6,4]
        Output= 1
        self.assertEqual(Output, get_sol().sumOfBeauties(nums))
    def test3(self):
        nums = [3,2,1]
        Output= 0
        self.assertEqual(Output, get_sol().sumOfBeauties(nums))
    # def test4(self):
    # def test5(self):
    # def test6(self):
