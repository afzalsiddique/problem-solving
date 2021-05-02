import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
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

class tester(unittest.TestCase):
    def test1(self):
        nums = [10, 5, 2, 6]
        k = 100
        Output= 8
        self.assertEqual(Output,Solution().numSubarrayProductLessThanK(nums,k))