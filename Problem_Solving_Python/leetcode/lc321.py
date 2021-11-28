import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    # see lc321.png
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def largest_arr(nums,k):
            n=len(nums)
            if k==0: return []
            st=[]
            for i in range(len(nums)):
                while n-i>k-len(st) and st and st[-1]<nums[i]:
                    st.pop()
                st.append(nums[i])
            return st

        def greater(nums1,i,nums2,j): # check if nums1[i] should be selected
            while i<len(nums1) and j<len(nums2) and nums1[i]==nums2[j]:
                i+=1
                j+=1
            if j==len(nums2): return True
            if i==len(nums1): return False
            return nums1[i]>nums2[j]

        def merge(nums1,nums2,length):
            li=[]
            li1=largest_arr(nums1,length)
            li2=largest_arr(nums2,k-length)
            i,j=0,0
            cnt=0
            while cnt!=k and i<len(li1) and j<len(li2):
                if greater(li1,i,li2,j):
                    li.append(li1[i])
                    i+=1
                else:
                    li.append(li2[j])
                    j+=1
                cnt+=1
            while cnt!=k and i<len(li1):
                li.append(li1[i])
                i+=1
                cnt+=1
            while cnt!=k and j<len(li2):
                li.append(li2[j])
                j+=1
                cnt+=1
            return li

        def larger_cmp(x):
            # if a number has more digits then it is larger.
            # if there are same number of digits then based on first number which is larger
            return (len(x),x)

        res=[float('-inf')]
        for i in range(1,k+1):
            res=max(res,merge(nums1,nums2,i),key=larger_cmp)
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        nums1,nums2,k = [3,4,6,5],  [9,1,2,5,8,3],  5
        Output= [9,8,6,5,3]
        self.assertEqual(Output, get_sol().maxNumber(nums1,nums2,k))
    def test2(self):
        nums1,nums2,k = [6,7],  [6,0,4],  5
        Output= [6,7,6,0,4]
        self.assertEqual(Output, get_sol().maxNumber(nums1,nums2,k))
    def test3(self):
        nums1,nums2,k = [3,9],  [8,9],  3
        Output= [9,8,9]
        self.assertEqual(Output, get_sol().maxNumber(nums1,nums2,k))
    def test4(self):
        nums1,nums2,k = [8,6,9], [1,7,5], 3
        Output= [9,7,5]
        self.assertEqual(Output, get_sol().maxNumber(nums1,nums2,k))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
