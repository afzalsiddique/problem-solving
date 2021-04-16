import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List


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

class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([1,3],Solution().largestDivisibleSubset([1,2,3]))
    def test2(self):
        self.assertEqual([1,2,4,8],Solution().largestDivisibleSubset([1,2,4,8]))
    def test3(self):
        self.assertEqual([4,8,240],Solution().largestDivisibleSubset([4,8,10,240]))
    def test4(self):
        self.assertEqual([2,4,8],Solution().largestDivisibleSubset([2,3,4,9,8]))
    def test5(self):
        self.assertEqual([1,2,4,8,16,32,64,128,456,512,1024,2048,4096,8192,16384],Solution().largestDivisibleSubset([1,2,4,8,16,32,64,128,456,512,1024,2048,4096,8192,16384]))
    def test6(self):
        self.assertEqual([1],Solution().largestDivisibleSubset([1]))
    def test7(self):
        self.assertEqual([2,4,8],Solution().largestDivisibleSubset([2,3,4,8]))






# wrong
class Solution2:
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
