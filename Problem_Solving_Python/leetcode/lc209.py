from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # two pointers approach
    def minSubArrayLen(self, target: int, A: List[int]) -> int:
        n=len(A)
        left,right=0,0
        res=float('inf')
        cur=0
        while right<n:
            while cur<target and right<n:
                cur+=A[right]
                right+=1
            if cur>=target:
                res=min(res,right-left)
            cur-=A[left]
            left+=1
        while cur>=target and left<right:
            res=min(res,right-left)
            cur-=A[left]
            left+=1
        return res if res!=float('inf') else 0
class Solution4:
    # two pointers approach
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        right, left = 0, 0
        summ = 0
        minn = float('inf')
        while right<n:
            summ += nums[right]
            right+=1
            while summ >= s:
                minn = min(minn, right-left)
                summ -= nums[left]
                left+=1
        return 0 if minn == float('inf') else minn
class Solution2:
    # binary search
    def minSubArrayLen(self, target: int, A: List[int]) -> int:
        A=[0]+list(accumulate(A))
        n=len(A)
        res=float('inf')
        for leftIdx,a in enumerate(A):
            rightIdx=bisect_left(A,a+target)
            if rightIdx!=n:
                res=min(res,rightIdx-leftIdx)
        return res if res!=float('inf') else 0
class Solution3:
    # two pointer
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        left=right=0
        summ=0
        minn=float('inf')
        while right<n:
            if summ<target:
                summ+=nums[right]
                right+=1
            else:
                summ-=nums[left]
                left+=1
            if summ>=target: minn=min(minn, right - left)
        while left<n:
            summ-=nums[left]
            left+=1
            if summ>=target: minn=min(minn, right - left)
        return minn if minn!=float('inf') else 0
class tester(unittest.TestCase):
    def test01(self):
        target = 7
        nums = [2,3,1,2,4,3]
        Output= 2
        self.assertEqual(Output,get_sol().minSubArrayLen(target,nums))
    def test02(self):
        target = 4
        nums = [1,4,4]
        Output= 1
        self.assertEqual(Output,get_sol().minSubArrayLen(target,nums))
    def test03(self):
        target = 11
        nums = [1,1,1,1,1,1,1,1]
        Output= 0
        self.assertEqual(Output,get_sol().minSubArrayLen(target,nums))
    def test04(self):
        self.assertEqual(3,get_sol().minSubArrayLen(11, [1,2,3,4,5]))
    def test05(self):
        self.assertEqual(5,get_sol().minSubArrayLen(15, [1,2,3,4,5]))
    # def test_6(self):
    # def test_7(self):
