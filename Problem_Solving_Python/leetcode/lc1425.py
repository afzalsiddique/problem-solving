import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # tle
    # lis
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dp=[nums[i] for i in range(n)]
        for i in range(n):
            for j in range(i):
                if i-j<=k:
                    dp[i]=max(dp[i],dp[j]+nums[i])
        return max(dp)
class tester(unittest.TestCase):
    def test1(self):
        nums = [10,2,-10,5,20]
        k = 2
        Output= 37
        self.assertEqual(Output,get_sol().constrainedSubsetSum(nums,k))
    def test2(self):
        nums = [-1,-2,-3]
        k = 1
        Output= -1
        self.assertEqual(Output,get_sol().constrainedSubsetSum(nums,k))
    def test3(self):
        nums = [10,-2,-10,-5,20]
        k = 2
        Output= 23
        self.assertEqual(Output,get_sol().constrainedSubsetSum(nums,k))
