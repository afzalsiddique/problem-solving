import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class MaxHeap(list):
    def __init__(self):
        super().__init__()
    def top(self): return -self[0][0],-self[0][1]
    def topElement(self): return -self[0][0]
    def topIndex(self): return -self[0][1]
    def push(self, element, idx): heappush(self, [-element, -idx])
    def heappop(self): return heappop(self)
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dp=[nums[i] for i in range(n)]
        maxHeap=MaxHeap()
        for i in range(n):
            lowest=i-k
            while maxHeap and maxHeap.topIndex()<lowest:
                maxHeap.heappop()
            if maxHeap:
                x,idx=maxHeap.top()
                dp[i]=max(dp[i],dp[idx]+nums[i])
            maxHeap.push(dp[i],i)
        return max(dp)
# class Solution2:
    # use monotonic queue
    # def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
class Solution3:
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

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(37,get_sol().constrainedSubsetSum([10,2,-10,5,20], 2))
    def test02(self):
        self.assertEqual(-1,get_sol().constrainedSubsetSum([-1,-2,-3], 1))
    def test03(self):
        self.assertEqual(23,get_sol().constrainedSubsetSum([10,-2,-10,-5,20], 2))
    def test04(self):
        self.assertEqual(16091,get_sol().constrainedSubsetSum([-8269,3217,-4023,-4138,-683,6455,-3621,9242,4015,-3790], 1))
    # def test05(self):
    # def test06(self):
