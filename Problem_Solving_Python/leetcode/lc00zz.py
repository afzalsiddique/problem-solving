from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def largest_arr(self,nums:List[int],k)->List[int]:
        # if k==0: return []
        n=len(nums)
        st=[]
        for i in range(n):
            while st and k-len(st)<=n-i-1 and st[-1]<nums[i]:
                st.pop()
            st.append(nums[i])
        while len(st)>k:
            st.pop()
        return st
    def greaterInFirstArray(self,nums1,i,nums2,j):
        m,n=len(nums1),len(nums2)
        while i<m and j<n and nums1[i]==nums2[j]:
            i+=1
            j+=1
        if j==n:
            return True
        if i==m:
            return False
        return nums1[i]>nums2[j]
    def merge(self,nums1,nums2):
        res=[]
        i=j=0
        while i<len(nums1) and j<len(nums2):
            if self.greaterInFirstArray(nums1,i,nums2,j):
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        while i<len(nums1):
            res.append(nums1[i])
            i+=1
        while j<len(nums2):
            res.append(nums2[j])
            j+=1
        return res


    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        maxx=[]
        for i in range(k+1):
            if len(nums1)<i:
                continue
            if len(nums2)<k-i:
                continue
            tmp1=self.largest_arr(nums1,i)
            tmp2=self.largest_arr(nums2,k-i)
            tmp=self.merge(tmp1,tmp2)
            maxx=max(maxx,tmp)
        return maxx


class MyTestCase(unittest.TestCase):
    def test00a1(self):
        self.assertEqual([6,7,8], get_sol().largest_arr([2,4,5,1,6,2,1,7,8],3))
    def test00a2(self):
        self.assertEqual([5,6,6], get_sol().largest_arr([5,5,6,6],3))
    def test00a3(self):
        self.assertEqual([9,8,7], get_sol().largest_arr([9,8,7],3))
    def test00a4(self):
        self.assertEqual([2,9,8], get_sol().largest_arr([2,1,1,9,8],3))
    def test00a5(self):
        self.assertEqual([7], get_sol().largest_arr([7,5],1))
    def test01(self):
        self.assertEqual([9,8,6,5,3], get_sol().maxNumber([3,4,6,5],  [9,1,2,5,8,3],  5))
    def test02(self):
        self.assertEqual([6,7,6,0,4], get_sol().maxNumber([6,7],  [6,0,4],  5))
    def test03(self):
        self.assertEqual([9,8,9], get_sol().maxNumber([3,9],  [8,9],  3))
    def test04(self):
        self.assertEqual([9,7,5], get_sol().maxNumber([8,6,9], [1,7,5], 3))
    def test05(self):
        self.assertEqual([9,7], get_sol().maxNumber([6,9], [7,5], 2))
    def test06(self):
        self.assertEqual([1,6,1,0,7], get_sol().maxNumber([1,6], [1,0,7], 5))
    def test07(self):
        self.assertEqual([9, 9, 9, 9, 9, 8, 7, 8, 8, 0, 9, 4, 5, 7, 0, 4, 0, 7, 6, 6, 5, 6, 2, 8, 6, 7, 1, 5, 0, 3, 2, 3, 9, 2, 1, 4, 8, 8, 1, 6, 3, 9, 5, 4, 3, 5, 9, 5, 4, 9, 3, 7, 9, 9, 1, 9, 9, 5, 6, 2, 4, 8, 1, 4, 0, 3, 0, 4, 2, 3, 2, 7, 6, 4, 8, 2, 1, 9, 4, 6, 0, 6, 0, 5, 2, 8, 6, 5, 9, 8, 2, 6, 1, 2, 1, 0, 6, 0, 1, 8, 8, 8, 7, 3, 1, 4, 9, 7, 0, 7, 7, 3, 8, 2, 8, 0, 5, 4, 7, 6, 1, 9, 8, 3, 5, 0, 4, 6, 2, 2, 5, 4, 9, 7, 4, 9, 1, 6, 7, 2, 0, 1, 2, 5, 8, 1, 1, 3, 2, 9, 9, 2, 1, 2, 3, 3, 6, 1, 8, 7], get_sol().maxNumber([9,3,9,4,3,6,6,1,8,3,6,5,8,9,0,4,0,7,6,6,5,6,2,8,6,7,1,5,0,3,2,3,9,2,1,4,8,8,1,6,3,9,5,4,3,5,9,5,4,9,3,7,9,9,1,9,9,5,6,2,4,8,1,4,0,3,0,4,2,3,2,7,6,4,8,2,1,9,4,6,0,6,0,5,2,8,6,5,9,8,2,6,1,2,1,0,6,0,1,8,8,8,7,3,1,4,9,7,0,7,7,3,8,2,8,0,5,4,7,6,1,9,8,3,5,0,4,6,2,2,5,4,9,7,4,9,1,6,7,2,0,1,2,5,8,1,1,3,2,9,9,2,1,2,3,3,6,1,8,7], [5,0,1,5,1,0,8,8,7,3,8,9,2,8,9,8,1,5,6,4,5,7,2,0,6,8,8,0,9,4,5,7], 160))
    def test08(self):
        self.assertEqual([9, 9, 9, 9, 9, 9, 9, 9, 7, 4, 1, 6, 3, 0, 4, 1, 4, 1, 8, 0, 3, 4, 4, 0, 3, 1, 2, 7, 9, 3, 2, 5, 5, 2, 7, 9, 5, 2, 2, 0, 2, 6, 7, 3, 0, 8, 8, 8, 6, 0, 1, 7, 8, 0, 2, 7, 5, 8, 7, 5, 2, 4, 0, 7, 3, 6, 3, 6, 3, 9, 6, 8, 1, 6, 9, 6, 2, 5, 9, 5, 1, 9, 2, 1, 4, 0, 7, 9, 8, 0, 4, 1, 0, 8, 7, 9, 7, 6, 6, 8, 8, 8, 3, 7, 5, 3, 2, 0, 4, 9, 1, 1, 3, 4, 9, 7, 9, 8, 4, 9, 6, 4, 7, 1, 9, 7, 4, 0, 4, 6, 0, 2, 0, 8, 9, 3, 0, 9, 9, 2], get_sol().maxNumber([3,9,9,6,9,6,2,1,1,7,7,7,1,4,9,9,6,9,5,3,6,4,6,3,8,2,5,1,1,7,9,2,3,7,4,0,3,4,4,0,2,6,7,3,0,8,8,8,6,0,1,7,8,0,2,7,5,8,7,5,2,4,0,7,3,6,3,6,3,9,6,8,1,6,9,6,2,5,9,5,1,9,2,1,4,0,7,9,8,0,4,1,0,8,7,9,7,6,6,8,8,8,3,7,5,3,2,0,4,9,1,1,3,4,9,7,9,8,4,9,6,4,7,1,9,7,4,0,4,6,0,2,0,8,9,3,0,9,9,2], [8,8,9,1,6,3,0,4,1,4,1,8,0,3,1,2,7,9,3,2,5,5,2,7,9,5,2,2], 140))
    def test09(self):
        self.assertEqual([9, 9, 9, 8, 8, 8, 7, 8, 6, 9, 4, 5, 3, 3, 7, 4, 3, 2, 8, 9, 8, 4, 1, 5, 5, 0, 5, 2, 8, 7, 8, 3, 3, 7, 9, 2, 0, 2, 0, 2, 2, 0, 4, 2, 2, 8, 6, 7, 1, 0, 8, 7, 5, 4, 6, 4, 1, 7, 4, 4, 3, 7, 5, 8, 8, 0, 3, 1, 3, 4, 6, 0, 6, 9, 6, 6, 4, 2, 1, 9, 3, 7, 4, 4, 4, 2, 1, 9, 5, 2, 1, 7, 6, 0, 1, 3, 5, 3, 7, 7], get_sol().maxNumber([5,7,7,0,1,6,7,2,2,4,6,8,9,2,0,9,8,7,6,3,9,4,8,8,4,5,3,3,7,4,3,2,8,9,8,4,0,2,0,2,2,0,4,2,2,8,6,7,1,0,8,7,5,4,6,4,1,7,4,4,3,7,5,8,8,0,3,1,3,4,6,0,6,9,6,6,4,2,1,9,3,7,4,4,4,2,1,9,5,2,1,7,6,0,1,3,5,3,7,7], [8,3,7,8,6,9,1,5,5,0,5,2,8,7,8,3,3,7,9,2], 100))
    def test10(self):
        self.assertEqual([8,5,9,5,2,6,4,3,8,4,1,6,9,1,0,7,2,9,2,8], get_sol().maxNumber([8,5,9,5,1,6,9], [2,6,4,3,8,4,1,0,7,2,9,2,8], 20))
