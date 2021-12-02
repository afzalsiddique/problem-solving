import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/cherry-pickup/discuss/329945/Very-easy-to-follow-%3A-step-by-step-recursive-backtracking-with-memoization-N4.
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dfs(r1,c1,r2,c2): # two person collecting at the same time
            if r1>=n or r2>=n or c1>=n or c2>=n: return float('-inf')
            if grid[r1][c1]==-1: return float('-inf')
            if grid[r2][c2]==-1: return float('-inf')
            if r1==n-1 and c1==n-1:
                return grid[r1][c1]
            if r2==n-1 and c2==n-1:
                return grid[r2][c2]

            if r1==r2 and c1==c2: # two persons standing at the same place. only one person will collect if any.
                ans=grid[r1][c1]
            else:
                ans=grid[r1][c1]+grid[r2][c2]

            tmp = max(dfs(r1+1,c1,r2+1,c2),
                      dfs(r1+1,c1,r2,c2+1),
                      dfs(r1,c1+1,r2+1,c2),
                      dfs(r1,c1+1,r2,c2+1)
                      )
            return ans+tmp

        n=len(grid)
        res= dfs(0,0,0,0)
        return res if res!=float('-inf') else 0
class Solution2:
    # wrong
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def dfs(i, j, end_i, end_j, dirs):
            if not 0<=i<n or not 0<=j<n: return [float('-inf'),[]]
            if grid[i][j]==-1: return [float('-inf'),[]]
            if i==end_i and j==end_j:
                return [grid[i][j],[(i,j)]]
            ans=float('-inf')
            path=[]
            for di,dj in dirs:
                tmp,tmp_path= dfs(i + di, j + dj, end_i, end_j, dirs)
                if tmp>ans:
                    ans=tmp
                    path=tmp_path
            return [grid[i][j]+ans,[(i,j)]+path]

        n=len(grid)
        dirs_go,dirs_comeback=[(1,0),(0,1)],[(-1,0),(0,-1)]
        go,path= dfs(0, 0, n - 1, n - 1, dirs_go)
        for i,j in path:
            grid[i][j]=0
        comeback,_= dfs(n - 1, n - 1, 0, 0, dirs_comeback)
        res=go+comeback
        return res if res!=float('-inf') else 0

class MyTestCase(unittest.TestCase):
    def test1(self):
        Output= 5
        self.assertEqual(Output, get_sol().cherryPickup(grid = [[0,1,-1],[1,0,-1],[1,1,1]]))
    def test2(self):
        Output= 0
        self.assertEqual(Output, get_sol().cherryPickup(grid = [[1,1,-1],[1,-1,1],[-1,1,1]]))
    def test3(self):
        grid = [[1,1,0,1],
                [0,0,0,0],
                [0,0,0,0],
                [1,0,1,1]]
        Output= 6
        self.assertEqual(Output, get_sol().cherryPickup(grid))
    def test4(self):
        grid=[[1,1,1,0,1],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [1,0,1,1,1]]
        Output= 8
        self.assertEqual(Output, get_sol().cherryPickup(grid))
    def test5(self):
        Output= 15
        self.assertEqual(Output, get_sol().cherryPickup(grid = [[1,1,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[1,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,1,1]]))
    # def test5(self):
    # def test6(self):
