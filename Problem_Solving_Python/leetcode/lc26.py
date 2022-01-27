from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        n=len(A)
        l,r=-1,0
        while r<n:
            l+=1
            A[l]=A[r]
            while r+1<n and A[l]==A[r+1]:
                r+=1
            r+=1
        return l+1
class Solution2:
    def removeDuplicates(self, A: List[int]) -> int:
        n=len(A)
        l,r=0,0
        while r<n:
            while r<n and A[l]==A[r]:
                r+=1
            l+=1
            if l<n and r<n:
                A[l]=A[r]
        return l
class Solution3:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j=0
        for i in range(1, n):
            if nums[i]!=nums[j]:
                nums[j+1] = nums[i]
                j+=1
        return j+1
class Solution4:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0 or n==1: return n
        l,r=0,0
        while r<n:
            if nums[l]==nums[r]:
                r+=1
                continue
            nums[l+1]=nums[r]
            l+=1
            r+=1
        return l+1



class MyTestCase(unittest.TestCase):
    def test01(self):
        nums=[1,1,2]
        length = get_sol().removeDuplicates(nums)
        expected = [1,2]
        self.assertEqual(length,len(expected))
        for x,y in zip(expected,nums):
            self.assertEqual(x,y)
    def test02(self):
        nums=[0,0,1,1,1,2,2,3,3,4]
        length = get_sol().removeDuplicates(nums)
        expected = [0,1,2,3,4]
        self.assertEqual(length,len(expected))
        for x,y in zip(expected,nums):
            self.assertEqual(x,y)
    # def test03(self):
    # def test04(self):
