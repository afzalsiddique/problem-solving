from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # time O(n*n) space O(n)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[float('inf') for _ in range(n)]
        dp[0]=triangle[0][0]
        for i in range(1,n):
            tmp_dp=[float('inf') for _ in range(n)]
            for j in range(i+1):
                if j==0:
                    tmp_dp[j]=triangle[i][j]+dp[j]
                elif j==i:
                    tmp_dp[j]=triangle[i][j]+dp[j-1]
                else:
                    tmp_dp[j]=triangle[i][j]+min(dp[j],dp[j-1])
            dp=tmp_dp
        return min(dp)
class Solution2:
    # time O(n*n) space O(n*n)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[float('inf')]*(col+1) for col in range(n)]
        dp[0][0]=triangle[0][0]
        for i in range(1,n):
            for j in range(i+1):
                if j==0:
                    dp[i][j]=triangle[i][j]+dp[i-1][j]
                elif j==i:
                    dp[i][j]=triangle[i][j]+dp[i-1][j-1]
                else:
                    dp[i][j]=triangle[i][j]+min(dp[i-1][j],dp[i-1][j-1])
        return min(dp[-1])
class Solution3:
    # time O(n*n) space O(n*n)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def dp(i,j):
            if j==len(triangle[i]): return float('inf')
            if i==len(triangle)-1: return triangle[i][j]
            return triangle[i][j]+min(dp(i+1,j),dp(i+1,j+1))

        return dp(0,0)
class Solution4:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(0,n):
            trail = [0] * (n-i-1)
            triangle[i] += trail
        dp = [[-1]*n for _ in range(n)]
        def helper(traingle, row, col, dp):
            n = len(triangle)
            if row==n-1:
                return triangle[row][col]
            if dp[row][col] != -1:
                return dp[row][col]
            bottom = helper(traingle, row+1, col, dp)
            bottom_right = helper(triangle, row+1, col+1, dp)
            dp[row][col] = triangle[row][col] + min(bottom, bottom_right)
            return dp[row][col]

        return helper(triangle, 0, 0, dp)
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(11, get_sol().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
    def test02(self):
        self.assertEqual(-10, get_sol().minimumTotal([[-10]]))
    # def test03(self):
