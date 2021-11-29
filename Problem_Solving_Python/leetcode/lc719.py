import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def valid(mid):
            res=0
            i,j=0,0
            while i<len(nums):
                while j<len(nums) and (nums[j]-nums[i])<=mid:
                    j+=1
                res+=j-i-1
                i+=1
            return res>=k

        nums.sort()
        lo,hi=0,nums[-1]-nums[0]
        while lo<=hi:
            mid=(lo+hi)//2
            if valid(mid):
                hi=mid-1
            else:
                lo=mid+1
        return lo



class MyTestCase(unittest.TestCase):
    def test_1(self):
        actual = get_sol().smallestDistancePair(nums = [1,3,1], k = 1)
        expected = 0
        self.assertEqual(expected, actual)
    def test_2(self):
        actual = get_sol().smallestDistancePair(nums = [1,6,1], k = 3)
        expected = 5
        self.assertEqual(expected, actual)
    def test_3(self):
        actual = get_sol().smallestDistancePair(nums = [1,1,1], k = 2)
        expected = 0
        self.assertEqual(expected, actual)
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
