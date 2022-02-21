from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:return mid
            if nums[l]==target: return l
            if nums[r]==target: return r
            if nums[l]<nums[mid]:
                if nums[l]<target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<target<nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1
class Solution5:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:return mid
            # if r-l+1<=3:
            #     if nums[l]==target: return l
            #     elif nums[r]==target: return r
            #     else: return -1
            # if nums[l]<nums[mid]:
            if nums[l]<=nums[mid]:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1
class Solution3:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]==target:
                return mid
            if nums[mid] <nums[r]:
                if nums[mid] < target <=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
        return -1
class Solution4:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        lo,hi=0,n-1
        while lo<=hi:
            mid=(lo+hi)//2

            if nums[mid]==target:
                return mid

            if nums[lo]<=nums[mid]:
                if nums[lo]<=target<=nums[mid]:
                    idx=bisect_left(nums,target,lo,hi)
                    return idx if idx!=n and nums[idx]==target else -1
                else:
                    lo=mid+1
            elif nums[mid]<=nums[hi]:
                if nums[mid]<=target<=nums[hi]:
                    idx=bisect_left(nums,target,lo,hi)
                    return idx if idx!=n and nums[idx]==target else -1
                else:
                    hi=mid-1
        return -1




class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(4, get_sol().search([4, 5, 6, 7, 0, 1, 2],0))
    def test02(self):
        self.assertEqual(-1, get_sol().search([4, 5, 6, 7, 0, 1, 2],3))
    def test03(self):
        self.assertEqual(-1, get_sol().search([1],0))
    def test04(self):
        self.assertEqual(0, get_sol().search([4, 5, 6, 7, 0, 1, 2],4))
    def test05(self):
        self.assertEqual(6, get_sol().search([4, 5, 6, 7, 0, 1, 2],2))
    def test06(self):
        self.assertEqual(2, get_sol().search([5, 6, 4],4))
    def test07(self):
        self.assertEqual(1, get_sol().search([4, 5, 6],5))
    def test08(self):
        self.assertEqual(2, get_sol().search([4, 5, 6],6))
    def test09(self):
        self.assertEqual(0, get_sol().search([4, 5],4))
    def test010(self):
        self.assertEqual(0, get_sol().search([5, 4],5))
    def test11(self):
        self.assertEqual(-1, get_sol().search([1, 3, 5], 2))
    def test12(self):
        self.assertEqual(0, get_sol().search([5, 1, 3], 5))
    def test13(self):
        self.assertEqual(1, get_sol().search([1, 3], 3))
    def test14(self):
        self.assertEqual(0, get_sol().search([6,7,1,2,3,4,5], 6))
    def test15(self):
        self.assertEqual(1, get_sol().search([3,1], 1))
    def test16(self):
        self.assertEqual(1, get_sol().search([5,1,2,3,4], 1))
    def test17(self):
        self.assertEqual(-1, get_sol().search([2,5,6,0,0,1,2], 3))