from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # sliding window template
    def numSubarrayProductLessThanK(self, A: List[int], k: int) -> int:
        n=len(A)
        right,left=0,0
        prod=1
        res=0
        while right<n:
            prod*=A[right]
            while left<=right and prod>=k:
                prod//=A[left]
                left+=1
            res+=right-left+1
            right+=1
        return res
class Solution4:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod //= nums[left]
                left += 1
            ans += right - left + 1
        return ans
class Solution2:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if n==0: return 0
        if n==1: return 1 if nums[0]<k else 0
        product,cnt= nums[0],0
        left,right=0,0
        while right<n:
            if product<k:
                cnt+=right-left+1
            if product>=k:
                if left==right:
                    right+=1
                    left+=1
                    if right<n:
                        product=nums[right]
                else:
                    product=product//nums[left]
                    left+=1
            else:
                right+=1
                if right<n:
                    product*=nums[right]
        return cnt
class Solution3:
    # tle
    # binary search
    def numSubarrayProductLessThanK(self, A: List[int], k: int) -> int:
        if k==0: return 0
        preProd=[1]+list(accumulate(A,lambda x,y:x*y))
        res=0
        for i,a in enumerate(A):
            right=i+1
            rightNum=preProd[right]
            leftNum=rightNum//k
            left=bisect_right(preProd,leftNum)
            if right>left:
                res+=right-left
        return res
class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(8,get_sol().numSubarrayProductLessThanK([10, 5, 2, 6],100,))
    def test02(self):
        self.assertEqual(0,get_sol().numSubarrayProductLessThanK([1,2,3],  0))
    def test03(self):
        self.assertEqual(0,get_sol().numSubarrayProductLessThanK([1,1,1], 1))
    def test04(self):
        self.assertEqual(6,get_sol().numSubarrayProductLessThanK([1,1,1], 2))
