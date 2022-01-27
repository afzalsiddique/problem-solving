from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        n=len(A)
        l,r=0,0
        while r<n:
            rTmp=r
            while r+1<n and A[rTmp]==A[r+1]:
                r+=1
            cnt=r-rTmp+1
            A[l]=A[r]
            l+=1
            if cnt>1:
                A[l]=A[r]
                l+=1
            r+=1
        return l
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j=0
        flag = False
        for i in range(1, n):
            if nums[i]==nums[j]:
                nums[j+1] = nums[i]
                flag = True
                if j+1!=i:nums[i]='ignore'
            else:
                if j+2<n and nums[j] == nums[j+1]:
                    nums[j+2] = nums[i]
                    if j+2!=i:nums[i]='ignore'
                    j+=2
                elif nums[i]!=nums[j]:
                    nums[j+1] = nums[i]
                    if j+1!=i:nums[i]='ignore'
                    j+=1
                flag = False
        if flag:
            return j+2
        return j+1

class MyTestCase(unittest.TestCase):
    def test01(self):
        nums=[1,1,1,2,2,3]
        length = get_sol().removeDuplicates(nums)
        expected = [1,1,2,2,3]
        self.assertEqual(length,len(expected))
        for x,y in zip(expected,nums):
            self.assertEqual(x,y)
    def test02(self):
        nums=[0,0,1,1,1,1,2,3,3]
        length = get_sol().removeDuplicates(nums)
        expected = [0,0,1,1,2,3,3]
        self.assertEqual(length,len(expected))
        for x,y in zip(expected,nums):
            self.assertEqual(x,y)
    # def test03(self):
    # def test04(self):
