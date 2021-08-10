import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # very bad code. need improvements
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        mapping={0:(0,1),1:(0,-1),2:(-1,0),3:(1,0)} # order: d_right,d_left,d_up,d_down
        INVALID=-2
        def initialize_dp(i,j,dir):
            if not 0<=i<m or not 0<=j<n: return 0
            if dp[dir][i][j]!=INVALID: return dp[dir][i][j]
            if grid[i][j]==0:
                dp[dir][i][j]=0
                return 0
            di,dj=mapping[dir]
            dp[dir][i][j]=1+initialize_dp(i+di,j+dj,dir)
            return dp[dir][i][j]

        m,n=len(grid),len(grid[0])
        dp=[[[INVALID for _ in range(n)] for __ in range(m)] for _ in range(4)]
        d_right=dp[0]
        d_left=dp[1]
        d_up=dp[2]
        d_down=dp[3]
        for i in range(m):
            for j in range(n):
                for dir in range(4):
                    initialize_dp(i,j,dir)

        res=-1
        for i in range(m):
            for j in range(n):
                for k in range(d_right[i][j]):
                    if j+k<n and d_down[i][j+k]>=k:
                        if i+k<m and j+k<n and d_left[i+k][j+k]>=k:
                            if i+k<m and d_up[i+k][j]>=k:
                                res=max(res,k+1)


        if res!=-1: return res*res
        return 0



class MyTestCase(unittest.TestCase):
    def test_1(self):
        grid = [[1,1,1],[1,0,1],[1,1,1]]
        Output= 9
        self.assertEqual(Output, get_sol().largest1BorderedSquare(grid))
    def test_2(self):
        grid = [[1,1,0,0]]
        Output= 1
        self.assertEqual(Output, get_sol().largest1BorderedSquare(grid))
    def test_3(self):
        grid = [[0]]
        Output= 0
        self.assertEqual(Output, get_sol().largest1BorderedSquare(grid))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
