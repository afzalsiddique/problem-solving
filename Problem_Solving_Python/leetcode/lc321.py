from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    # see lc321.png
    def largest_arr(self,nums,k):
        n=len(nums)
        if k==0: return []
        st=[]
        for i in range(len(nums)):
            # n-i>k-len(st) => no of items left > no of items we need
            while n-i>k-len(st) and st and st[-1]<nums[i]:
                st.pop()
            st.append(nums[i])
        return st
    def greaterElementInFirstArray(self,nums1,i,nums2,j): # check if nums1[i] should be selected
        while i<len(nums1) and j<len(nums2) and nums1[i]==nums2[j]:
            i+=1
            j+=1
        if j==len(nums2): return True
        if i==len(nums1): return False
        return nums1[i]>nums2[j]
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def merge(nums1,nums2,length): # take 'length' no of elements from nums1 and 'k - length' no of elemnts from nums2
            li=[]
            li1=self.largest_arr(nums1,length)
            li2=self.largest_arr(nums2,k-length)
            i=j=cnt=0
            while cnt!=k and i<len(li1) and j<len(li2):
                if self.greaterElementInFirstArray(li1,i,li2,j):
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

        def listCmp(x):
            # if a number has more digits then it is larger.
            # if there are same number of digits then based on first number which is larger
            return (len(x),x)

        res=[float('-inf')]
        for i in range(1,k+1):
            res=max(res,merge(nums1,nums2,i),key=listCmp)
        return res

class Solution2:
    # tle
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        @cache
        def dp(i,j,k):
            if k==0:
                return []
            res=[]
            select1,not_select1,select2,not_select2=[],[],[],[]
            if i<m:
                not_select1=dp(i+1,j,k)
                select1=[nums1[i]]+dp(i+1,j,k-1)
            if j<n:
                not_select2=dp(i,j+1,k)
                select2=[nums2[j]]+dp(i,j+1,k-1)
            if len(not_select1)==k:
                res=max(res,not_select1)
            if len(select1)==k:
                res=max(res,select1)
            if len(not_select2)==k:
                res=max(res,not_select2)
            if len(select2)==k:
                res=max(res,select2)
            return res

        m,n=len(nums1),len(nums2)
        return dp(0,0,k)

class Solution3:
    # tle
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        @cache
        def dp(i,j,k):
            if k==1:
                one=right_max1[i] if i<m else float('-inf')
                two=right_max2[j] if j<n else float('-inf')
                return max(one,two)
            if i==m and j==n: return float('-inf')
            ans1,ans2,ans3,ans4=float('-inf'),float('-inf'),float('-inf'),float('-inf')
            if j==n:
                curDigit=nums1[i]*10**(k-1)
                ans1=curDigit+dp(i+1,j,k-1)
                ans3=dp(i+1,j,k)
            elif i==m:
                curDigit=nums2[j]*10**(k-1)
                ans2=curDigit+dp(i,j+1,k-1)
                ans4=dp(i,j+1,k)
            else:
                ans1=nums1[i]*10**(k-1)+dp(i+1,j,k-1)
                ans2=nums2[j]*10**(k-1)+dp(i,j+1,k-1)
                ans3=dp(i+1,j,k)
                ans4=dp(i,j+1,k)
            return max(ans1,ans2,ans3,ans4)

        right_max1=list(accumulate(nums1[::-1],max))[::-1]
        right_max2=list(accumulate(nums2[::-1],max))[::-1]
        m,n=len(nums1),len(nums2)
        return list(map(int,str(dp(0,0,k))))
class MyTestCase(unittest.TestCase):
    def test00a1(self):
        self.assertEqual([6,7,8], get_sol().largest_arr([2,4,5,1,6,2,1,7,8],3))
    def test00a2(self):
        self.assertEqual([5,6,6], get_sol().largest_arr([5,5,6,6],3))
    def test00a3(self):
        self.assertEqual([9,8,7], get_sol().largest_arr([9,8,7],3))
    def test00a4(self):
        self.assertEqual([2,9,8], get_sol().largest_arr([2,1,1,9,8],3))
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
        self.assertEqual([9, 9, 9, 9, 9, 8, 7, 8, 8, 0, 9, 4, 5, 7, 0, 4, 0, 7, 6, 6, 5, 6, 2, 8, 6, 7, 1, 5, 0, 3, 2, 3, 9, 2, 1, 4, 8, 8, 1, 6, 3, 9, 5, 4, 3, 5, 9, 5, 4, 9, 3, 7, 9, 9, 1, 9, 9, 5, 6, 2, 4, 8, 1, 4, 0, 3, 0, 4, 2, 3, 2, 7, 6, 4, 8, 2, 1, 9, 4, 6, 0, 6, 0, 5, 2, 8, 6, 5, 9, 8, 2, 6, 1, 2, 1, 0, 6, 0, 1, 8, 8, 8, 7, 3, 1, 4, 9, 7, 0, 7, 7, 3, 8, 2, 8, 0, 5, 4, 7, 6, 1, 9, 8, 3, 5, 0, 4, 6, 2, 2, 5, 4, 9, 7, 4, 9, 1, 6, 7, 2, 0, 1, 2, 5, 8, 1, 1, 3, 2, 9, 9, 2, 1, 2, 3, 3, 6, 1, 8, 7], get_sol().maxNumber([9,3,9,4,3,6,6,1,8,3,6,5,8,9,0,4,0,7,6,6,5,6,2,8,6,7,1,5,0,3,2,3,9,2,1,4,8,8,1,6,3,9,5,4,3,5,9,5,4,9,3,7,9,9,1,9,9,5,6,2,4,8,1,4,0,3,0,4,2,3,2,7,6,4,8,2,1,9,4,6,0,6,0,5,2,8,6,5,9,8,2,6,1,2,1,0,6,0,1,8,8,8,7,3,1,4,9,7,0,7,7,3,8,2,8,0,5,4,7,6,1,9,8,3,5,0,4,6,2,2,5,4,9,7,4,9,1,6,7,2,0,1,2,5,8,1,1,3,2,9,9,2,1,2,3,3,6,1,8,7], [5,0,1,5,1,0,8,8,7,3,8,9,2,8,9,8,1,5,6,4,5,7,2,0,6,8,8,0,9,4,5,7], 160))
    def test07(self):
        self.assertEqual([9, 9, 9, 9, 9, 9, 9, 9, 7, 4, 1, 6, 3, 0, 4, 1, 4, 1, 8, 0, 3, 4, 4, 0, 3, 1, 2, 7, 9, 3, 2, 5, 5, 2, 7, 9, 5, 2, 2, 0, 2, 6, 7, 3, 0, 8, 8, 8, 6, 0, 1, 7, 8, 0, 2, 7, 5, 8, 7, 5, 2, 4, 0, 7, 3, 6, 3, 6, 3, 9, 6, 8, 1, 6, 9, 6, 2, 5, 9, 5, 1, 9, 2, 1, 4, 0, 7, 9, 8, 0, 4, 1, 0, 8, 7, 9, 7, 6, 6, 8, 8, 8, 3, 7, 5, 3, 2, 0, 4, 9, 1, 1, 3, 4, 9, 7, 9, 8, 4, 9, 6, 4, 7, 1, 9, 7, 4, 0, 4, 6, 0, 2, 0, 8, 9, 3, 0, 9, 9, 2], get_sol().maxNumber([3,9,9,6,9,6,2,1,1,7,7,7,1,4,9,9,6,9,5,3,6,4,6,3,8,2,5,1,1,7,9,2,3,7,4,0,3,4,4,0,2,6,7,3,0,8,8,8,6,0,1,7,8,0,2,7,5,8,7,5,2,4,0,7,3,6,3,6,3,9,6,8,1,6,9,6,2,5,9,5,1,9,2,1,4,0,7,9,8,0,4,1,0,8,7,9,7,6,6,8,8,8,3,7,5,3,2,0,4,9,1,1,3,4,9,7,9,8,4,9,6,4,7,1,9,7,4,0,4,6,0,2,0,8,9,3,0,9,9,2], [8,8,9,1,6,3,0,4,1,4,1,8,0,3,1,2,7,9,3,2,5,5,2,7,9,5,2,2], 140))
    def test08(self):
        self.assertEqual([9, 9, 9, 8, 8, 8, 7, 8, 6, 9, 4, 5, 3, 3, 7, 4, 3, 2, 8, 9, 8, 4, 1, 5, 5, 0, 5, 2, 8, 7, 8, 3, 3, 7, 9, 2, 0, 2, 0, 2, 2, 0, 4, 2, 2, 8, 6, 7, 1, 0, 8, 7, 5, 4, 6, 4, 1, 7, 4, 4, 3, 7, 5, 8, 8, 0, 3, 1, 3, 4, 6, 0, 6, 9, 6, 6, 4, 2, 1, 9, 3, 7, 4, 4, 4, 2, 1, 9, 5, 2, 1, 7, 6, 0, 1, 3, 5, 3, 7, 7], get_sol().maxNumber([5,7,7,0,1,6,7,2,2,4,6,8,9,2,0,9,8,7,6,3,9,4,8,8,4,5,3,3,7,4,3,2,8,9,8,4,0,2,0,2,2,0,4,2,2,8,6,7,1,0,8,7,5,4,6,4,1,7,4,4,3,7,5,8,8,0,3,1,3,4,6,0,6,9,6,6,4,2,1,9,3,7,4,4,4,2,1,9,5,2,1,7,6,0,1,3,5,3,7,7], [8,3,7,8,6,9,1,5,5,0,5,2,8,7,8,3,3,7,9,2], 100))
