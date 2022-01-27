from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    # longest common subsequence
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(i,j):
            if i==len(nums1):
                return 0
            if j==len(nums2):
                return 0
            if nums1[i]==nums2[j]:
                return 1+dp(i+1,j+1)
            return max(dp(i+1,j),dp(i,j+1))

        return dp(0,0)
class Solution2:
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

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(2,get_sol().maxUncrossedLines([1,4,2],[1,2,4]))
    def test02(self):
        self.assertEqual(3,get_sol().maxUncrossedLines([2,5,1,2,5],[10,5,2,1,5,2]))
    def test03(self):
        self.assertEqual(2,get_sol().maxUncrossedLines([1,3,7,1,7,5],[1,9,2,5,1]))
    def test04(self):
        self.assertEqual(11,get_sol().maxUncrossedLines([5,1,2,5,1,2,2,3,1,1,1,1,1,3,1],[2,5,1,3,4,5,5,2,2,4,5,2,2,3,1,4,5,3,2,4,5,2,4,4,2,2,2,1,3,1]))
