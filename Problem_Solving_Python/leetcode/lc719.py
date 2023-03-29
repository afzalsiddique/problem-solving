import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def has_at_least_k_pair_with_at_most_d_difference(d):
            res=0
            i,j=0,0
            while i<len(nums):
                while j<len(nums) and (nums[j]-nums[i])<=d:
                    j+=1
                res+=j-i-1
                i+=1
            return res>=k

        nums.sort()
        lo,hi=0,nums[-1]-nums[0]
        while lo<=hi:
            mid=(lo+hi)//2
            if has_at_least_k_pair_with_at_most_d_difference(mid):
                hi=mid-1
            else:
                lo=mid+1
        return lo



class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(0, get_sol().smallestDistancePair(nums = [1,3,1], k = 1))
    def test02(self):
        self.assertEqual(5, get_sol().smallestDistancePair(nums = [1,6,1], k = 3))
    def test03(self):
        self.assertEqual(0, get_sol().smallestDistancePair(nums = [1,1,1], k = 2))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
