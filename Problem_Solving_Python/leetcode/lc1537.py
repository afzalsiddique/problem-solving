import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD=10**9+7
        m,n=len(nums1),len(nums2)
        sum1,sum2=0,0
        i,j=0,0
        res=0
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                sum1+=nums1[i]
                i+=1
            elif nums2[j]<nums1[i]:
                sum2+=nums2[j]
                j+=1
            else:
                res+=max(sum1,sum2)
                res+=nums1[i]
                i+=1
                j+=1
                sum1,sum2=0,0
        while i<m:
            sum1+=nums1[i]
            i+=1
        while j<n:
            sum2+=nums2[j]
            j+=1

        res+=max(sum1,sum2)
        return res % MOD
class Solution2:
    # wrong
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD=10**9+7
        @functools.lru_cache(None)
        def f(i,j,cur):
            if i==m:
                if cur==1:
                    return (sum(nums2[j:])) % MOD
                return 0
            if j==n:
                if cur==0:
                    return (sum(nums1[i:])) % MOD
                return 0
            if nums1[i]==nums2[j]:
                option1=f(i+1,j+1,0)
                option2=f(i+1,j+1,1)
                return (nums1[i]+max(option1, option2)) % MOD
            elif nums1[i]<nums2[j]:
                if cur==0:
                    tmp=f(i+1,j,cur)
                    return (nums1[i]+tmp) % MOD
                else:
                    tmp=f(i+1,j,cur)
                    return tmp % MOD
            elif nums1[i]>nums2[j]:
                if cur==0:
                    tmp=f(i,j+1,cur)
                    return tmp % MOD
                else:
                    tmp=f(i,j+1,cur)
                    return (nums2[j]+tmp) % MOD

        m,n=len(nums1),len(nums2)
        ans1=f(0,0,0)
        ans2=f(0,0,1)
        res=max(ans1,ans2)
        return res % MOD

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(30, get_sol().maxSum([2,4,5,8,10], [4,6,8,9]))
    def test2(self):
        self.assertEqual(109, get_sol().maxSum([1,3,5,7,9], [3,5,100]))
    def test3(self):
        self.assertEqual(40, get_sol().maxSum([1,2,3,4,5], [6,7,8,9,10]))
    def test4(self):
        self.assertEqual(30, get_sol().maxSum([2,4,5,8,10], [4,6,8]))
    # def test5(self):
    # def test6(self):
    # def test7(self):
