from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional,Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
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
    def nextGreater(self,nums):
        n=len(nums)
        res=[-1]*n
        st=[]
        for i in range(n):
            while st and nums[st[-1]]<nums[i]:
                idx=st.pop()
                res[idx]=nums[i]
            st.append(i)
        return res
    def merge(self,nums1,nums2):
        res=[]
        i=j=0
        nxt1=self.nextGreater(nums1)
        nxt2=self.nextGreater(nums2)
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                if nxt1[i]>nxt2[j]:
                    res.append(nums1[i])
                    i+=1
                else:
                    res.append(nums2[j])
                    j+=1
            elif nums1[i]>nums2[j]:
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

class Correct:
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


class Tester(unittest.TestCase):
    def test01(self):
        a,b,k=[1,6], [1,0,7], 5
        self.assertEqual(Correct().maxNumber(a,b,k), Solution().maxNumber(a,b,k))
