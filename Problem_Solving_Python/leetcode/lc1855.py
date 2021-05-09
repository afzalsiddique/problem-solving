import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()

class Solution:
    # two pointer
    def maxDistance(self, n1: List[int], n2: List[int]) -> int:
        i = j = res = 0
        while i < len(n1) and j < len(n2):
            if n1[i] > n2[j]:
                i += 1
            else:
                res = max(res, j - i)
                j += 1
        return res
class Solution2:
    # binary search
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        def mybisect_right(A, x):
            # A is a non-increasing
            left, right = 0, len(A)-1
            while left <= right:
                mid = (left+right)//2 # right mid
                if x <= A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

            return right

        ans = 0
        for i, x in enumerate(nums1):
            j = mybisect_right(nums2,x)
            ans = max(ans, j-i)

        return ans
class tester(unittest.TestCase):
    def test01(self):
        nums1 = [55,30,5,4,2]
        nums2 = [100,20,10,10,5]
        Output= 2
        self.assertEqual(Output,get_sol().maxDistance(nums1,nums2))
    def test02(self):
        nums1 = [2,2,2]
        nums2 = [10,10,1]
        Output= 1
        self.assertEqual(Output,get_sol().maxDistance(nums1,nums2))
    def test03(self):
        nums1 = [30,29,19,5]
        nums2 = [25,25,25,25,25]
        Output= 2
        self.assertEqual(Output,get_sol().maxDistance(nums1,nums2))
    def test04(self):
        nums1 = [5,4]
        nums2 = [3,2]
        Output= 0
        self.assertEqual(Output,get_sol().maxDistance(nums1,nums2))
