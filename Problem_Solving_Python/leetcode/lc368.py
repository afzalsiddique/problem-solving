from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution2()
class Solution:
    # https://www.youtube.com/watch?v=Wv6DlL0Sawg
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums.sort()
        dp=[1]*n
        maxx=1 # to find out subset
        for i in range(1,n):
            for j in range(i):
                if nums[i]%nums[j]==0:
                    dp[i]=max(dp[i],1+dp[j])
                    if maxx<dp[i]:
                        maxx=dp[i]

        # construct the subset
        res=[]
        prev=-1
        for i in reversed(range(n)):
            if dp[i]==maxx and (prev%nums[i]==0 or prev==-1):
                res.append(nums[i])
                prev=nums[i]
                maxx-=1
        return res


class Solution2:
    def largestDivisibleSubset(self, A: List[int]) -> List[int]:
        n=len(A)
        A.sort()
        dp=[1]*n
        last_indices=[-1]*n
        for i in range(n):
            for j in range(i):
                if A[i]%A[j]==0:
                    if dp[j]+1>dp[i]:
                        dp[i]=dp[j]+1
                        last_indices[i]=j

        li=[]
        maxLength=max(dp)
        idx=n-1
        while dp[idx]!=maxLength:
            idx-=1
        while len(li)!=maxLength:
            li.append(A[idx])
            idx=last_indices[idx]
        return li
# wrong
class Solution3:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp={}
        nums.sort()
        def is_div_subset(nums):
            if len(nums)==1: return True
            for i in range(len(nums)-1,0,-1):
                for j in range(i-1,-1,-1):
                    if nums[i]%nums[j]: return False
            return True

        def helper(nums):
            if is_div_subset(nums): return nums[:]
            if tuple(nums) in dp: return dp[tuple(nums)]
            maxx=[]
            maxx_len=float('-inf')
            for i in range(len(nums)):
                temp=nums[:i]+nums[i+1:]
                if tuple(temp) in dp: return dp[tuple(temp)]
                ans = helper(temp)
                if len(ans)>maxx_len:
                    maxx_len=len(ans)
                    maxx=ans
            dp[tuple(nums)]=maxx[:]
            return dp[tuple(nums)]

        ans = helper(nums)
        print(dp)
        return ans
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertIn(sorted(get_sol().largestDivisibleSubset([1,2,3])),[[1,2],[1,3]])
    def test02(self):
        self.assertEqual([1,2,4,8], sorted(get_sol().largestDivisibleSubset([1,2,4,8])))
    def test03(self):
        self.assertIn(sorted(get_sol().largestDivisibleSubset([108,540,90])),[[108,540],[90,540]])
    def test04(self):
        self.assertEqual([1], sorted(get_sol().largestDivisibleSubset([1])))
    def test05(self):
        self.assertEqual([2,4,8], sorted(get_sol().largestDivisibleSubset([2,3,4,9,8])))
    def test06(self):
        self.assertEqual([4,8,240], sorted(get_sol().largestDivisibleSubset([4,8,10,240])))
    def test07(self):
        self.assertEqual([2,4,8], sorted(get_sol().largestDivisibleSubset([2,3,4,8])))
    def test08(self):
        self.assertEqual([9,18,90,180,360,720], sorted(get_sol().largestDivisibleSubset([5,9,18,54,108,540,90,180,360,720])))
