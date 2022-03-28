import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
# ***************** nums[i] != nums[i + 1] for all valid i ***************
class Solution:
    def findPeakElement(self, A: List[int]) -> int:
        n=len(A)
        if n==1: return 0
        if A[0]>A[1]: return 0
        if A[-1]>A[-2]: return n-1
        lo,hi=0,n-1
        while lo<=hi:
            m=(lo+hi)//2
            if A[m]>A[m-1] and A[m]>A[m+1]:
                return m
            if A[m+1]>A[m]:
                lo=m+1
            else:
                hi=m-1
class Solution2:
    def findPeakElement(self, nums: List[int]) -> int:
        lo,hi=0,len(nums)-1
        while lo<hi:
            mid1=(lo+hi)//2
            mid2=mid1+1
            if nums[mid1]<nums[mid2]:
                lo=mid2
            else:
                hi=mid1
        return lo
class Solution4:
    # https://www.youtube.com/watch?v=a7D77DdhlFc
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        lo,hi=0,n-1
        while lo<=hi:
            mid = (lo+hi)//2
            if (mid==0 or nums[mid-1]<nums[mid]) and (mid==n-1 or nums[mid]>nums[mid+1]):
                return mid
            elif mid>0 and nums[mid-1]>nums[mid]:
                hi=mid-1
            else:
                lo=mid+1
        return lo
class Solution3:
    # bad solution
    # this one should work even without the restriction " nums[i] != nums[i + 1] for all valid i "
    # time O(n)
    # it is easier to do a normal linear solution than this solution
    def findPeakElement(self, nums: List[int]) -> int:
        def my_binary_search(lo,hi):
            if lo>hi: return float('-inf')
            mid = (lo+hi)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            ans1 = my_binary_search(lo,mid-1)
            ans2 = my_binary_search(mid+1,hi)
            return max(ans1,ans2) # the reason it is max(ans1,ans2) is because we are returning float('-inf') when lo>hi

        nums = [float('-inf')] + nums + [float('-inf')]
        n=len(nums)
        lo,hi=1, n-2
        ans = my_binary_search(lo,hi)
        ans-=1 # convert to original array
        return ans

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(2, get_sol().findPeakElement([1,2,3,1]))
    def test02(self):
        self.assertEqual(3, get_sol().findPeakElement([10,80,10,30,10,20,10]))
    def test03(self):
        self.assertEqual(5, get_sol().findPeakElement([1,2,1,3,5,6,4]))
    def test04(self):
        self.assertEqual(0, get_sol().findPeakElement([1]))
