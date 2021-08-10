import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=4: return 0
        nums.sort()
        minn=float('inf')
        for i in range(0,3+1):
            j=n-(3-i)-1
            tmp=nums[j]-nums[i]
            minn=min(minn,tmp)
        return minn

class Tester(unittest.TestCase):
    def test_1(self):
        nums = [5,3,2,4]
        Output= 0
        self.assertEqual(Output,get_sol().minDifference(nums))
    def test_2(self):
        nums = [1,5,0,10,14]
        Output= 1
        self.assertEqual(Output,get_sol().minDifference(nums))
    def test_3(self):
        nums = [6,6,0,1,1,4,6]
        Output= 2
        self.assertEqual(Output,get_sol().minDifference(nums))
    def test_4(self):
        nums = [1,5,6,14,15]
        Output= 1
        self.assertEqual(Output,get_sol().minDifference(nums))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):