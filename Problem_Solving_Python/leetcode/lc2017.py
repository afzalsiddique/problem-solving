import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # [X, X, X, X, X, ., ., ., ., ., ]
    # [., ., ., ., X, X, X, X, X, X, ]
    # robot2_score = max(top_right portion, bottom_left portion)
    # try to minimize robot2_score
    def gridGame(self, grid: List[List[int]]) -> int:
        def get_sum_range(l,r,pre): # both inclusive
            return pre[r+1]-pre[l]
        m,n=2,len(grid[0])
        pre_sum = []
        pre_sum.append([0]+list(itertools.accumulate(grid[0])))
        pre_sum.append([0]+list(itertools.accumulate(grid[1])))
        robot2=float('inf')
        for i in range(n):
            robot2 = min(robot2,max(get_sum_range(0,i-1,pre_sum[1]), get_sum_range(i+1,n-1,pre_sum[0])))
        return robot2
class Solution2:
    # wrong ans
    def gridGame(self, grid: List[List[int]]) -> int:
        def dfs(i,j,dp):
            if not 0<=i<m or not 0<=j<n: return float('-inf')
            if dp[i][j]!=-1: return dp[i][j]
            if i==1 and j==n-1:
                dp[i][j]=grid[i][j]
                return grid[i][j]
            for di,dj in [(1,0),(0,1)]:
                x,y=i+di,j+dj
                dp[i][j] = max(dp[i][j],grid[i][j]+dfs(x,y,dp))
            return dp[i][j]
        def get_path(dp):
            i,j=1,n-1
            path = [(i,j)]
            while (i,j)!=(0,0):
                if j==0:
                    i-=1
                    path.append((i,j))
                elif i==0:
                    j-=1
                    path.append((i,j))
                elif dp[i-1][j]>dp[i][j-1]:
                    i-=1
                    path.append((i,j))
                else:
                    j-=1
                    path.append((i,j))
            return path

        m,n=2,len(grid[0])
        dp1=[[-1]*n for _ in range(m)]
        dp2=[[-1]*n for _ in range(m)]
        robot1 = dfs(0,0,dp1)
        print(robot1)
        for x in dp1: print(x)
        path = get_path(dp1)
        for (i,j) in path: grid[i][j]=0
        for x in grid: print(x)
        return dfs(0,0,dp2)

class MyTestCase(unittest.TestCase):
    def test1(self):
        grid = [[2,5,4],[1,5,1]]
        Output= 4
        self.assertEqual(Output, get_sol().gridGame(grid))
    def test2(self):
        grid = [[3,3,1],[8,5,2]]
        Output= 4
        self.assertEqual(Output, get_sol().gridGame(grid))
    def test3(self):
        grid = [[1,3,1,15],[1,3,3,1]]
        Output= 7
        self.assertEqual(Output, get_sol().gridGame(grid))
    def test4(self):
        grid = [[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]]
        Output= 63
        self.assertEqual(Output, get_sol().gridGame(grid))
    # def test5(self):
    # def test6(self):
