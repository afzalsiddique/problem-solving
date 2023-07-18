from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def divide(l,r):
            if l>=r:
                return
            m=(l+r)//2
            divide(l,m)
            divide(m+1,r)
            merge(l,m,r)

        def merge(l,m,r):
            li=[]
            i,j=l,m+1
            while i<=m and j<=r:
                if nums[i]<nums[j]:
                    li.append(nums[i])
                    i+=1
                else:
                    li.append(nums[j])
                    j+=1
            while i<=m:
                li.append(nums[i])
                i+=1
            while j<=r:
                li.append(nums[j])
                j+=1
            i=0
            while i<len(li):
                nums[l]=li[i]
                l+=1
                i+=1

        divide(0,len(nums)-1)
        return nums




class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual([1,3,4,5], get_sol().sortArray([5,3,4,1]))
    def test02(self):
        self.assertEqual([1], get_sol().sortArray([1]))
    def test03(self):
        self.assertEqual([1,2], get_sol().sortArray([2,1]))
    def test04(self):
        self.assertEqual([1,2,3], get_sol().sortArray([3,2,1]))
    def test05(self):
        self.assertEqual([1,2,2,3,5], get_sol().sortArray([2,5,2,1,3]))
    def test06(self):
        self.assertEqual([1,2,2,5], get_sol().sortArray([2,5,2,1]))
    def test07(self):
        self.assertEqual([-7, -5, -4, -1, -1, 0, 0, 4, 7, 9], get_sol().sortArray([-4,0,7,4,9,-5,-1,0,-7,-1]))
