import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1344908/Python-3-DP-Explanation-with-pictures.
    def maxPoints(self, points: List[List[int]]) -> int:
        m,n=len(points),len(points[0])
        dp=[[-1]*n for _ in range(m)]
        for j in range(n):
            dp[0][j]=points[0][j]
        for i in range(1,m):
            left=[0 for _ in range(n)]
            right=[0 for _ in range(n)]
            for j in range(n):
                if j==0:
                    left[j]=dp[i-1][j]
                else:
                    left[j]=max(left[j-1]-1,dp[i-1][j])
            for j in reversed(range(n)):
                if j==n-1:
                    right[j]=dp[i-1][j]
                else:
                    right[j]=max(right[j+1]-1,dp[i-1][j])
            for j in range(n):
                dp[i][j]=points[i][j]+ max(left[j],right[j])
        return max(dp[-1])

class tester(unittest.TestCase):
    def test_1(self):
        points = [[1,2,3],[1,5,1],[3,1,1]]
        Output= 9
        self.assertEqual(Output,get_sol().maxPoints(points))
    def test_2(self):
        points = [[1,5],[2,3],[4,2]]
        Output= 11
        self.assertEqual(Output,get_sol().maxPoints(points))
    def test_3(self):
        points = [[1,5,7,9]]
        Output= 9
        self.assertEqual(Output,get_sol().maxPoints(points))
    def test_4(self):
        points = [[1],[5],[7],[9]]
        Output= 22
        self.assertEqual(Output,get_sol().maxPoints(points))
    def test_5(self):
        points = [[0,3,0,4,2],[5,4,2,4,1],[5,0,0,5,1],[2,0,1,0,3]]
        Output= 15
        self.assertEqual(Output,get_sol().maxPoints(points))
    # def test_6(self):
    # def test_7(self):