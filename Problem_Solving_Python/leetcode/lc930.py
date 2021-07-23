import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        di=defaultdict(int)
        di[0]=1 # for subarrays starting from the very beginnning
        cumsum=itertools.accumulate(nums)
        ans=0
        for x in cumsum:
            ans+=di[x-goal]
            di[x]+=1
        return ans
class tester(unittest.TestCase):
    def test_1(self):
        nums = [1,0,1,0,1]
        goal = 2
        Output= 4
        self.assertEqual(Output,get_sol().numSubarraysWithSum(nums,goal))
    def test_2(self):
        nums = [0,0,0,0,0]
        goal = 0
        Output= 15
        self.assertEqual(Output,get_sol().numSubarraysWithSum(nums,goal))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):