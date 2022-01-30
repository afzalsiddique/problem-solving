import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
checkInput=True # check if original grid is changed after function call
class Solution:
    # fill the land around the boundary
    def numEnclaves(self, grid: List[List[int]]) -> int:
        LAND=1;WATER=0;VIS=-1
        def dfs(x,y):
            if not 0<=x<m or not 0<=y<n:
                return float('-inf')
            if grid[x][y]==WATER:
                return 0
            if grid[x][y]==VIS:
                return 0
            grid[x][y]=VIS
            res=1
            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                res+=dfs(x+dx,y+dy)
            return res

        m,n=len(grid),len(grid[0])
        for i in range(m): # fill the land around the boundary
            dfs(i,0)
            dfs(i,n-1)
        for j in range(n): # fill the land around the boundary
            dfs(0,j)
            dfs(m-1,j)

        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==LAND and grid[i][j]!=VIS:
                    tmp=dfs(i,j)
                    if tmp!=float('-inf'):
                        res+=tmp
        for i in range(m): # restore original grid
            for j in range(n):
                if grid[i][j]==VIS:
                    grid[i][j]=LAND
        return res

class Tester(unittest.TestCase):
    def test01(self):
        grid = [[0,0,0,0],
                [1,0,1,0],
                [0,1,1,0],
                [0,0,0,0]]
        gridCopy=[row[:] for row in grid]
        self.assertEqual(3,get_sol().numEnclaves(grid))
        self.assertEqual(gridCopy,grid)
    def test02(self):
        grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
        gridCopy=[row[:] for row in grid]
        self.assertEqual(0,get_sol().numEnclaves(grid))
        self.assertEqual(gridCopy,grid)
    def test03(self):
        grid = [[0,0,0,1,1,1,0,1,0,0],
                [1,1,0,0,0,1,0,1,1,1],
                [0,0,0,1,1,1,0,1,0,0],
                [0,1,1,0,0,0,1,0,1,0],
                [0,1,1,1,1,1,0,0,1,0],
                [0,0,1,0,1,1,1,1,0,1],
                [0,1,1,0,0,0,1,1,1,1],
                [0,0,1,0,0,1,0,1,0,1],
                [1,0,1,0,1,1,0,0,0,0],
                [0,0,0,0,1,1,0,0,0,1]
                ]
        self.assertEqual(3,get_sol().numEnclaves(grid))
        gridCopy=[row[:] for row in grid]
        self.assertEqual(gridCopy,grid)
