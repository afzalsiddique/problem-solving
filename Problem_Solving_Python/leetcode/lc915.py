import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/partition-array-into-disjoint-intervals/discuss/175945/Java-one-pass-7-lines/181596
    def partitionDisjoint(self, nums: List[int]) -> int:
        n=len(nums)
        idx=0
        max_left=nums[0] # we assume that it max_left is the max of left partition
        cur_max=nums[0]
        for i in range(1,n):
            if nums[i]<max_left: # our assumption is incorrect
                max_left=cur_max # lets update our assumption
                idx=i # update partition index
            else:
                cur_max=max(cur_max,nums[i]) # keep track of current max
        return idx+1
class Solution2:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n=len(nums)
        left_max=[0]*n # max from the left side
        right_min=[float('inf')]*n # min from the right side
        for i in range(n):
            if i==0:
                left_max[0]=nums[0]
                continue
            if nums[i]>left_max[i-1]:
                left_max[i]=nums[i]
            else:
                left_max[i]=left_max[i-1]
        for i in range(n-1,-1,-1):
            if i==n-1:
                right_min[-1]=nums[-1]
                continue
            if nums[i]<right_min[i+1]:
                right_min[i]=nums[i]
            else:
                right_min[i]=right_min[i+1]
        # print(left_max)
        # print(right_min)
        for i in range(n-1):
            if left_max[i]<=right_min[i+1]:
                return i+1


class tester(unittest.TestCase):
    def test_1(self):
        nums,Output = [5,0,3,8,6], 3
        self.assertEqual(Output, get_sol().partitionDisjoint(nums))
    def test_2(self):
        nums,Output = [1,1,1,0,6,12], 4
        self.assertEqual(Output, get_sol().partitionDisjoint(nums))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):