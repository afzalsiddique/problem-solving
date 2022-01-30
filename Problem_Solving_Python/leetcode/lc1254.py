import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
checkInput=True # check if original grid is changed after function call
class Solution:
    # First fill the land around the boundary, then count the remaining islands
    def closedIsland(self, grid: List[List[int]]) -> int:
        LAND=0;WATER=1;VIS=-1
        def dfs(x,y):
            if not 0<=x<m or not 0<=y<n:
                return
            if grid[x][y]==WATER:
                return
            if grid[x][y]==VIS:
                return
            grid[x][y]=VIS
            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                dfs(x+dx,y+dy)

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
                    dfs(i,j)
                    res+=1
        for i in range(m): # restore original grid
            for j in range(n):
                if grid[i][j]==VIS:
                    grid[i][j]=LAND
        return res
class Solution2:
    def closedIsland(self, grid: List[List[int]]) -> int:
        VIS=-1
        def dfs(x,y):
            if not 0<=x<m or not 0<=y<n:
                return False
            if grid[x][y]==1:
                return True
            if grid[x][y]==VIS:
                return True
            grid[x][y]=VIS
            res=True
            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                if not dfs(x+dx,y+dy):
                    res=False # don't return. 'Flood Fill'
            return res

        m,n=len(grid),len(grid[0])
        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0 and grid[i][j]!=VIS:
                # if grid[i][j]==0: # also works. because if we visit 0, then we mark it VIS
                    res+=dfs(i,j)
        for i in range(m): # retrieve the original grid
            for j in range(n):
                if grid[i][j]==VIS:
                    grid[i][j]=0
        return res

class Tester(unittest.TestCase):
    def test1(self):
        grid = [[1,1,1,1,1,1,1,0],
                [1,0,0,0,0,1,1,0],
                [1,0,1,0,1,1,1,0],
                [1,0,0,0,0,1,0,1],
                [1,1,1,1,1,1,1,0]]
        gridCopy=[row[:] for row in grid]
        self.assertEqual(2,get_sol().closedIsland(grid))
        self.assertEqual(gridCopy if checkInput else True,grid if checkInput else True) # change if the original grid has been changed
    def test2(self):
        grid = [[0,0,1,0,0],
                [0,1,0,1,0],
                [0,1,1,1,0]]
        gridCopy=[row[:] for row in grid]
        self.assertEqual(1,get_sol().closedIsland(grid))
        self.assertEqual(gridCopy if checkInput else True,grid if checkInput else True) # change if the original grid has been changed
    def test3(self):
        grid = [[1,1,1,1,1,1,1],
                [1,0,0,0,0,0,1],
                [1,0,1,1,1,0,1],
                [1,0,1,0,1,0,1],
                [1,0,1,1,1,0,1],
                [1,0,0,0,0,0,1],
                [1,1,1,1,1,1,1]]
        gridCopy=[row[:] for row in grid]
        self.assertEqual(2,get_sol().closedIsland(grid))
        self.assertEqual(gridCopy if checkInput else True,grid if checkInput else True) # change if the original grid has been changed
    def test4(self):
        grid = [[0,0,1,1,0,1,0,0,1,0],
                [1,1,0,1,1,0,1,1,1,0],
                [1,0,1,1,1,0,0,1,1,0],
                [0,1,1,0,0,0,0,1,0,1],
                [0,0,0,0,0,0,1,1,1,0],
                [0,1,0,1,0,1,0,1,1,1],
                [1,0,1,0,1,1,0,0,0,1],
                [1,1,1,1,1,1,0,0,0,0],
                [1,1,1,0,0,1,0,1,0,1],
                [1,1,1,0,1,1,0,1,1,0]]
        gridCopy=[row[:] for row in grid]
        self.assertEqual(5,get_sol().closedIsland(grid))
        self.assertEqual(gridCopy if checkInput else True,grid if checkInput else True) # change if the original grid has been changed
    def test5(self):
        grid = [[1,1,1,1],
                [1,0,0,1],
                [1,1,1,1]]
        gridCopy=[row[:] for row in grid]
        self.assertEqual(1,get_sol().closedIsland(grid))
        self.assertEqual(gridCopy,grid)
    def test6(self):
        grid = [[0,0,0],
                [1,0,1],
                [1,1,0] ]
        gridCopy=[row[:] for row in grid]
        self.assertEqual(0,get_sol().closedIsland(grid))
        self.assertEqual(gridCopy if checkInput else True,grid if checkInput else True) # change if the original grid has been changed
