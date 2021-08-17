import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minSideJumps(self, A):
        dp = [1, 0, 1]
        for lane in A:
            lane-=1 # convert to zero based indexing
            if lane!=-1:
                dp[lane] = float('inf')
            for i in range(3):
                if lane != i:
                    dp[i] = min(dp[i], dp[(i + 1) % 3] + 1, dp[(i + 2) % 3] + 1)
        return min(dp)
class Solution2:
    def minSideJumps(self, A):
        n=len(A)
        dp = [[0]*3 for _ in range(n)]
        dp[0]=[1,0,1]
        for i in range(1,n):
            lane=A[i]
            lane-=1
            if lane==-1:
                for j in range(3):
                    dp[i][j] = min(dp[i-1][j], dp[i-1][(j + 1) % 3] + 1, dp[i-1][(j + 2) % 3] + 1)
            else:
                dp[i][lane]=float('inf')
                dp[i-1][lane]=float('inf')
                for j in range(3):
                    if j==lane: continue
                    dp[i][j] = min(dp[i-1][j], dp[i-1][(j + 1) % 3] + 1, dp[i-1][(j + 2) % 3] + 1)
        return min(dp[-1])


class MyTestCase(unittest.TestCase):
    def test_1(self):
        obstacles = [0,1,2,3,0]
        Output= 2
        self.assertEqual(Output, get_sol().minSideJumps(obstacles))
    def test_2(self):
        obstacles = [0,1,1,3,3,0]
        Output= 0
        self.assertEqual(Output, get_sol().minSideJumps(obstacles))
    def test_3(self):
        obstacles = [0,2,1,0,3,0]
        Output= 2
        self.assertEqual(Output, get_sol().minSideJumps(obstacles))
    def test_4(self):
        obstacles = [0,0,3,1,0,1,0,2,3,1,0]
        Output= 2
        self.assertEqual(Output, get_sol().minSideJumps(obstacles))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
