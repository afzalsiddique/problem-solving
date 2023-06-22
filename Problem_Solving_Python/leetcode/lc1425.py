from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
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

class Solution4:
    # tle
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        @cache
        def dp(i):
            if i>=n:
                return 0
            res=float('-inf')
            for j in range(i, i+k):
                tmp1=nums[i]
                tmp2=dp(j+1)
                res=max(res,tmp1,tmp1 + tmp2)
            return res

        n=len(nums)
        res=float('-inf')
        for i in range(n):
            res=max(res, dp(i))
        return res
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(37,get_sol().constrainedSubsetSum([10,2,-10,5,20], 2))
    def test02(self):
        self.assertEqual(-1,get_sol().constrainedSubsetSum([-1,-2,-3], 1))
    def test03(self):
        self.assertEqual(23,get_sol().constrainedSubsetSum([10,-2,-10,-5,20], 2))
    def test04(self):
        self.assertEqual(16091,get_sol().constrainedSubsetSum([-8269,3217,-4023,-4138,-683,6455,-3621,9242,4015,-3790], 1))
    def test05(self):
        self.assertEqual(12,get_sol().constrainedSubsetSum([10,2,-10], 2))
    # def test06(self):
