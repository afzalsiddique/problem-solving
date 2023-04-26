import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution3:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        pre = []
        curSum = sum(nums[i] for i in range(k-1))
        for i in range(k-1,len(nums)):
            curSum+=nums[i]
            pre.append(curSum)
            curSum-=nums[i-k+1]

        n=len(pre)
        left_max=[None]*n # index
        right_max=[None]*n # index
        idx=0
        for i in range(len(pre)-k):
            if pre[i]>pre[idx]: # '>' because find the smallest index for left side
                idx=i
            left_max[i]=idx

        idx=n-1
        for i in range(len(pre)-1,k-1,-1):
            if pre[i]>=pre[idx]: # '>=' because find the smallest index for right side
                idx=i
            right_max[i]=idx

        maxIdx=[None,None,None]
        maxSum=float('-inf')
        for i in range(n):
            left_fake_idx,right_fake_idx=i-k,i+k
            if not left_fake_idx>=0 or not right_fake_idx<n: continue
            left,right=left_max[left_fake_idx], right_max[right_fake_idx]
            curIdx=[left,i,right]
            tmpSum=pre[left]+pre[i]+pre[right]
            if tmpSum>maxSum:
                maxIdx=[left,i,right]
                maxSum=tmpSum
            elif tmpSum==maxSum:
                maxIdx=min(maxIdx,curIdx)
        return maxIdx
class Solution:
    # https://www.youtube.com/watch?v=wN1nPANp3hk
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        # calculate prefix sum
        pre=[] # prefix sum
        cur=0 # current_sum/running_sum
        left,right=0,0
        while right<k-1:
            cur+=nums[right]
            right+=1
        while right<n:
            cur+=nums[right]
            pre.append(cur)
            cur-=nums[left]
            left+=1
            right+=1

        left_max=[0]*len(pre) # index. first k are invalid
        right_max=[0]*len(pre) # index. last k are invalid
        idx=0
        for i in range(len(pre)-k):
            if pre[i]>pre[idx]:
                idx=i
            left_max[i+k]=idx

        idx=len(pre)-1
        for i in range(len(pre)-1,k-1,-1): # first k and last k values from the prefix sum are invalid
            if pre[i]>=pre[idx]:
                idx=i
            right_max[i-k]=idx
        # print(pre)
        # print(left_max)
        # print(right_max)

        maxx=float('-inf')
        for i in range(k,len(pre)-k):
            if pre[i]+pre[left_max[i]]+pre[right_max[i]]>maxx:
                res=[left_max[i],i,right_max[i]]
                maxx=pre[i]+pre[left_max[i]]+pre[right_max[i]]
        return res

class Solution2:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        # calculate prefix sum
        pre=[]
        cur=0
        left,right=0,0
        while right<k-1:
            cur+=nums[right]
            right+=1
        while right<n:
            cur+=nums[right]
            pre.append(cur)
            cur-=nums[left]
            left+=1
            right+=1

        left_max=[(float('-inf'),-1)]*len(pre) # (val,index)
        right_max=[(float('-inf'),-1)]*len(pre) # (val,index)
        cur=(float('-inf'),-1)
        for i in range(len(pre)-k):
        # for i in range(len(pre)): # should also work
            if pre[i]>cur[0]:
                cur=(pre[i],i)
            left_max[i+k]=cur

        cur=(float('-inf'),-1)
        for i in range(len(pre)-1,k-1,-1):
        # for i in range(len(pre)-1,-1,-1): # should also work
            if pre[i]>=cur[0]:
                cur=(pre[i],i)
            right_max[i-k]=cur

        maxx=float('-inf')
        for i in range(len(pre)):
            if pre[i]+left_max[i][0]+right_max[i][0]>maxx:
                res=[left_max[i][1],i,right_max[i][1]]
                maxx=pre[i]+left_max[i][0]+right_max[i][0]
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual([0,3,5], get_sol().maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1],  2))
    def test2(self):
        self.assertEqual([0,2,4], get_sol().maxSumOfThreeSubarrays([1,2,1,2,1,2,1,2,1],  2))
    def test3(self):
        self.assertEqual([3,8,14], get_sol().maxSumOfThreeSubarrays([17,9,3,2,7,10,20,1,13,4,5,16,4,1,17,6,4,19,8,3],  4))
    def test4(self):
        self.assertEqual([0,1,4], get_sol().maxSumOfThreeSubarrays([17,9,3,2,7] ,1))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
