import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m,n=len(A),len(B)
        A=['#'] + A
        B=['#'] + B
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if A[i]==B[j]:
                    dp[i][j]=1+dp[i-1][j-1]
        return max(map(max,dp))


class tester(unittest.TestCase):
    def test1(self):
        nums1 = [1,2,3,2,1]
        nums2 = [3,2,1,4,7]
        Output= 3
        self.assertEqual(Output,Solution().findLength(nums1,nums2))
    def test2(self):
        nums1 = [0,0,0,0,0]
        nums2 = [0,0,0,0,0]
        Output= 5
        self.assertEqual(Output,Solution().findLength(nums1,nums2))
    def test3(self):
        nums1 = [0,1,1,1,1]
        nums2 = [1,0,1,0,1]
        Output= 2
        self.assertEqual(Output,Solution().findLength(nums1,nums2))
    def test4(self):
        nums1 = [1,0,0,0,1]
        nums2 = [1,0,0,1,1]
        Output= 3
        self.assertEqual(Output,Solution().findLength(nums1,nums2))


