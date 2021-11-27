import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
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
            if pre[i]>cur[0]:
                cur=(pre[i],i)
            left_max[i+k]=cur

        cur=(float('-inf'),-1)
        for i in range(len(pre)-1,k-1,-1):
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
        nums,k = [1,2,1,2,6,7,5,1],  2
        Output= [0,3,5]
        self.assertEqual(Output, get_sol().maxSumOfThreeSubarrays(nums,k))
    def test2(self):
        nums,k = [1,2,1,2,1,2,1,2,1],  2
        Output= [0,2,4]
        self.assertEqual(Output, get_sol().maxSumOfThreeSubarrays(nums,k))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
