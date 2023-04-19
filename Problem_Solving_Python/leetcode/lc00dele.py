from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    # see lc321.png
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def largest_arr(nums,k):
            n=len(nums)
            if k==0: return []
            st=[]
            for i in range(len(nums)):
                # n-i>k-len(st) => no of items left > no of items we need
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
    def test5(self):
        nums1,nums2,k = [6,9], [7,5], 2
        Output= [9,7]
        self.assertEqual(Output, get_sol().maxNumber(nums1,nums2,k))
    def test6(self):
        nums1,nums2,k = [9,3,9,4,3,6,6,1,8,3,6,5,8,9,0,4,0,7,6,6,5,6,2,8,6,7,1,5,0,3,2,3,9,2,1,4,8,8,1,6,3,9,5,4,3,5,9,5,4,9,3,7,9,9,1,9,9,5,6,2,4,8,1,4,0,3,0,4,2,3,2,7,6,4,8,2,1,9,4,6,0,6,0,5,2,8,6,5,9,8,2,6,1,2,1,0,6,0,1,8,8,8,7,3,1,4,9,7,0,7,7,3,8,2,8,0,5,4,7,6,1,9,8,3,5,0,4,6,2,2,5,4,9,7,4,9,1,6,7,2,0,1,2,5,8,1,1,3,2,9,9,2,1,2,3,3,6,1,8,7], [5,0,1,5,1,0,8,8,7,3,8,9,2,8,9,8,1,5,6,4,5,7,2,0,6,8,8,0,9,4,5,7], 160
        Output= [9, 9, 9, 9, 9, 8, 7, 8, 8, 0, 9, 4, 5, 7, 0, 4, 0, 7, 6, 6, 5, 6, 2, 8, 6, 7, 1, 5, 0, 3, 2, 3, 9, 2, 1, 4, 8, 8, 1, 6, 3, 9, 5, 4, 3, 5, 9, 5, 4, 9, 3, 7, 9, 9, 1, 9, 9, 5, 6, 2, 4, 8, 1, 4, 0, 3, 0, 4, 2, 3, 2, 7, 6, 4, 8, 2, 1, 9, 4, 6, 0, 6, 0, 5, 2, 8, 6, 5, 9, 8, 2, 6, 1, 2, 1, 0, 6, 0, 1, 8, 8, 8, 7, 3, 1, 4, 9, 7, 0, 7, 7, 3, 8, 2, 8, 0, 5, 4, 7, 6, 1, 9, 8, 3, 5, 0, 4, 6, 2, 2, 5, 4, 9, 7, 4, 9, 1, 6, 7, 2, 0, 1, 2, 5, 8, 1, 1, 3, 2, 9, 9, 2, 1, 2, 3, 3, 6, 1, 8, 7]
        self.assertEqual(Output, get_sol().maxNumber(nums1,nums2,k))
    def test7(self):
        self.assertEqual([9, 9, 9, 9, 9, 9, 9, 9, 7, 4, 1, 6, 3, 0, 4, 1, 4, 1, 8, 0, 3, 4, 4, 0, 3, 1, 2, 7, 9, 3, 2, 5, 5, 2, 7, 9, 5, 2, 2, 0, 2, 6, 7, 3, 0, 8, 8, 8, 6, 0, 1, 7, 8, 0, 2, 7, 5, 8, 7, 5, 2, 4, 0, 7, 3, 6, 3, 6, 3, 9, 6, 8, 1, 6, 9, 6, 2, 5, 9, 5, 1, 9, 2, 1, 4, 0, 7, 9, 8, 0, 4, 1, 0, 8, 7, 9, 7, 6, 6, 8, 8, 8, 3, 7, 5, 3, 2, 0, 4, 9, 1, 1, 3, 4, 9, 7, 9, 8, 4, 9, 6, 4, 7, 1, 9, 7, 4, 0, 4, 6, 0, 2, 0, 8, 9, 3, 0, 9, 9, 2], get_sol().maxNumber([3,9,9,6,9,6,2,1,1,7,7,7,1,4,9,9,6,9,5,3,6,4,6,3,8,2,5,1,1,7,9,2,3,7,4,0,3,4,4,0,2,6,7,3,0,8,8,8,6,0,1,7,8,0,2,7,5,8,7,5,2,4,0,7,3,6,3,6,3,9,6,8,1,6,9,6,2,5,9,5,1,9,2,1,4,0,7,9,8,0,4,1,0,8,7,9,7,6,6,8,8,8,3,7,5,3,2,0,4,9,1,1,3,4,9,7,9,8,4,9,6,4,7,1,9,7,4,0,4,6,0,2,0,8,9,3,0,9,9,2], [8,8,9,1,6,3,0,4,1,4,1,8,0,3,1,2,7,9,3,2,5,5,2,7,9,5,2,2], 140))
    # def test8(self):
