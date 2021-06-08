import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # longest common subsequence
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m,n=len(nums1),len(nums2)
        dp = [[-1]*n for _ in range(m)]
        def helper(i,j):
            if i==m or j==n: return 0
            if dp[i][j] != -1: return dp[i][j]
            if nums1[i]==nums2[j]:
                dp[i][j]=max(dp[i][j],helper(i+1,j+1)+1)
            else:
                dp[i][j]=max(helper(i+1,j),helper(i,j+1))
            return dp[i][j]
        return helper(0,0)

class tester(unittest.TestCase):
    def test1(self):
        nums1 = [1,4,2]
        nums2 = [1,2,4]
        Output= 2
        self.assertEqual(Output,get_sol().maxUncrossedLines(nums1,nums2))
    def test2(self):
        nums1 = [2,5,1,2,5]
        nums2 = [10,5,2,1,5,2]
        Output= 3
        self.assertEqual(Output,get_sol().maxUncrossedLines(nums1,nums2))
    def test3(self):
        nums1 = [1,3,7,1,7,5]
        nums2 = [1,9,2,5,1]
        Output= 2
        self.assertEqual(Output,get_sol().maxUncrossedLines(nums1,nums2))
    def test4(self):
        nums1 = [5,1,2,5,1,2,2,3,1,1,1,1,1,3,1]
        nums2 = [2,5,1,3,4,5,5,2,2,4,5,2,2,3,1,4,5,3,2,4,5,2,4,4,2,2,2,1,3,1]
        Output= 11
        self.assertEqual(Output,get_sol().maxUncrossedLines(nums1,nums2))