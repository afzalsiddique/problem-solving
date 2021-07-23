import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # two pointers approach
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        right, left = 0, 0
        summ = 0
        minn = float('inf')
        while right<n:
            summ += nums[right]
            right+=1
            while summ >= s:
                minn = min(minn, right-left)
                summ -= nums[left]
                left+=1
        return 0 if minn == float('inf') else minn
class Solution2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        left=right=0
        summ=0
        minn=float('inf')
        while right<n:
            if summ<target:
                summ+=nums[right]
                right+=1
            else:
                summ-=nums[left]
                left+=1
            if summ>=target: minn=min(minn, right - left)
        while left<n:
            summ-=nums[left]
            left+=1
            if summ>=target: minn=min(minn, right - left)
        return minn if minn!=float('inf') else 0
class tester(unittest.TestCase):
    def test_1(self):
        target = 7
        nums = [2,3,1,2,4,3]
        Output= 2
        self.assertEqual(Output,get_sol().minSubArrayLen(target,nums))
    def test_2(self):
        target = 4
        nums = [1,4,4]
        Output= 1
        self.assertEqual(Output,get_sol().minSubArrayLen(target,nums))
    def test_3(self):
        target = 11
        nums = [1,1,1,1,1,1,1,1]
        Output= 0
        self.assertEqual(Output,get_sol().minSubArrayLen(target,nums))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
