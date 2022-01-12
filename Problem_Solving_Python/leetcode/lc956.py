import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/tallest-billboard/discuss/219700/Python-DP-clean-solution(1D)
    def tallestBillboard(self, rods: List[int]) -> int:
        dp=defaultdict(int)
        dp[0]=0
        for rod in rods:
            cur=dp.copy()
            for totalSum, posSum in dp.items():
                cur[totalSum+rod]=max(cur[totalSum+rod],dp[totalSum]+rod)
                cur[totalSum-rod]=max(cur[totalSum-rod],dp[totalSum])
                cur[totalSum]=max(cur[totalSum],dp[totalSum])
            dp=cur
        return dp[0]
class Solution2:
    # tle. dfs
    def tallestBillboard(self, rods: List[int]) -> int:
        def helper(i,left,right,remain):
            nonlocal res
            if left==right:
                res=max(res,left)
            if i==n:
                return
            if left+right+remain<2*res:
                return
            if abs(right-left)>remain:
                return
            helper(i+1,left+rods[i],right,remain-rods[i]) # use it for left support
            helper(i+1,left,right+rods[i],remain-rods[i]) # use it for right support
            helper(i+1,left,right,remain) # do not use it for any supports

        n=len(rods)
        res=0
        helper(0,0,0,sum(rods))
        return res
class Solution3:
    # tle
    def tallestBillboard(self, rods: List[int]) -> int:
        def isOn(mask:int,i:int):
            return mask&(1<<i)
        def getNums(mask:int):
            li=[]
            for i in range(n):
                if isOn(mask,i):
                    li.append(rods[i])
            return li

        n=len(rods)
        res=float('-inf')
        for mask in range(2**n-1,-1,-1):
            nums=getNums(mask)
            if self.canPartition(nums):
                res=max(res,sum(nums)//2)
        return res


    def canPartition(self, nums: List[int]) -> bool: # leetcode 416
        @functools.lru_cache(None)
        def helper(start,target):
            if target==0:
                return True
            for i in range(start,n):
                if helper(i+1,target-nums[i]):
                    return True
            return False

        n=len(nums)
        if sum(nums)%2: return False
        return helper(0,sum(nums)//2)

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(6, get_sol().tallestBillboard([1,2,3,6]))
    def test2(self):
        self.assertEqual(10, get_sol().tallestBillboard([1,2,3,4,5,6]))
    def test3(self):
        self.assertEqual(0, get_sol().tallestBillboard([1,2]))
    def test4(self):
        self.assertEqual(1023, get_sol().tallestBillboard([1,2,4,8,16,32,64,128,256,512,50,50,50,150,150,150,100,100,100,123]))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
