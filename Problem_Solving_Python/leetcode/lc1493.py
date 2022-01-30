import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    def kadanes(self,A:List[int]):
        n=len(A)
        maxEndingHere=[0]*n
        maxEndingHere[0]=A[0]
        for i in range(1,n):
            if A[i]==0:
                maxEndingHere[i]=0
            else:
                maxEndingHere[i]=maxEndingHere[i-1]+1
        return maxEndingHere
    def longestSubarray(self, A: List[int]) -> int:
        n=len(A)
        maxEndingHere=self.kadanes(A)
        maxStartingHere=self.kadanes(A[::-1])[::-1]
        maxStartingHere[-1]=A[-1]
        res=float('-inf')

        # option1
        for i in range(1,n-1):
            res=max(res,maxEndingHere[i-1]+maxStartingHere[i+1])
            if A[i+1]==0:
                res=max(res,maxEndingHere[i],maxStartingHere[i])

        # option2
        # for i in range(n-2):
        #     res=max(res,maxEndingHere[i]+maxStartingHere[i+2])
        #     if A[i]==0:
        #         res=max(res,maxEndingHere[i+1],maxStartingHere[i+1])
        return res
class Solution4:
    def longestSubarray(self, A: List[int]) -> int:
        n=len(A)
        res=0

        maxEndingHere=[0]*n
        maxEndingHere[0]=A[0]
        for i in range(1,n):
            if A[i]==0:
                maxEndingHere[i]=0
            else:
                maxEndingHere[i]=maxEndingHere[i-1]+1

        maxStartingHere=[0]*n
        maxStartingHere[-1]=A[-1]
        for i in range(n-2,-1,-1):
            if A[i]==0:
                maxStartingHere[i]=0
            else:
                maxStartingHere[i]=maxStartingHere[i+1]+1

        # option1
        for i in range(1,n-1):
            res=max(res,maxEndingHere[i-1]+maxStartingHere[i+1])
            if A[i+1]==0:
                res=max(res,maxEndingHere[i],maxStartingHere[i])

        # option2
        # for i in range(n-2):
        #     res=max(res,maxEndingHere[i]+maxStartingHere[i+2])
        #     if A[i]==0:
        #         res=max(res,maxEndingHere[i+1],maxStartingHere[i+1])
        return res
class Solution2:
    # wrong
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        max_ending_here=[0]*n
        max_starting_here=[0]*n
        cnt=0
        for i in range(n):
            if nums[i]==1:
                cnt+=1
            else:
                cnt=0
            max_ending_here[i]=cnt
        cnt=0
        for i in reversed(range(n)):
            if nums[i]==1:
                cnt+=1
            else:
                cnt=0
            max_starting_here[i]=cnt

        res=0
        # print(max_ending_here)
        # print(max_starting_here)
        for i in range(n-2):
            res=max(res,max_ending_here[i]+max_starting_here[i+2])
        return res
class Solution3:
    # wrong. Exactly one element must be deleted
    def longestSubarray(self, A: List[int]) -> int:
        n=len(A)
        l,r=0,0
        res=0
        zeros=0
        while r<n:
            while r<n and zeros<=1:
                if not A[r]:
                    zeros+=1
                r+=1
            res=max(res,r-l-zeros)
            while l<r and zeros>1:
                if not A[l]:
                    zeros-=1
                l+=1
        return res


class MyTestCase(unittest.TestCase):
    def test1(self):
        nums = [1,1,0,1]
        Output= 3
        self.assertEqual(Output,get_sol().longestSubarray(nums))
    def test2(self):
        nums = [0,1,1,1,0,1,1,0,1]
        Output= 5
        self.assertEqual(Output,get_sol().longestSubarray(nums))
    def test3(self):
        nums = [1,1,1]
        Output= 2
        self.assertEqual(Output,get_sol().longestSubarray(nums))
    def test4(self):
        nums = [1,1,0,0,1,1,1,0,1]
        Output= 4
        self.assertEqual(Output,get_sol().longestSubarray(nums))
    def test5(self):
        nums = [0,0,0]
        Output= 0
        self.assertEqual(Output,get_sol().longestSubarray(nums))
    def test06(self):
        nums = [0,1,0]
        Output= 1
        self.assertEqual(Output,get_sol().longestSubarray(nums))
