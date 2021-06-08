import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n=len(nums)
        maxx=float('-inf')
        nums.sort()
        for i in range(n//2):
            maxx=max(maxx,nums[i]+nums[n-1-i])
        return maxx
class tester(unittest.TestCase):
    def test1(self):
        nums = [3,5,2,3]
        Output= 7
        self.assertEqual(Output,get_sol().minPairSum(nums))
    def test2(self):
        nums = [3,5,4,2,4,6]
        Output= 8
        self.assertEqual(Output,get_sol().minPairSum(nums))
