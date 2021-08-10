import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        prev_color=grid[row][col]
        BORDER_COLOR=-1
        vis=set()
        def dfs(i,j):
            if (i,j) in vis: return
            vis.add((i,j))
            if i==0 or i==m-1 or j==0 or j==n-1:
                grid[i][j]=BORDER_COLOR
            for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                new_i,new_j=i+di,j+dj
                if 0<=new_i<m and 0<=new_j<n:
                    if grid[new_i][new_j]==prev_color:
                        dfs(new_i,new_j)
                    elif grid[new_i][new_j]!=prev_color and grid[new_i][new_j]!=BORDER_COLOR:
                        grid[i][j]=BORDER_COLOR


        dfs(row,col)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==BORDER_COLOR:
                    grid[i][j]=color
        return grid

class MyTestCase(unittest.TestCase):
    def test_1(self):
        grid,row,col,color= [[1,1],[1,2]], 0, 0,3
        Output= [[3,3],[3,2]]
        self.assertEqual(Output, get_sol().colorBorder(grid,row,col,color))
    def test_2(self):
        grid,row,col,color= [[1,2,2],[2,3,2]], 0, 1,3
        Output= [[1,3,3],[2,3,3]]
        self.assertEqual(Output, get_sol().colorBorder(grid,row,col,color))
    def test_3(self):
        grid,row,col,color= [[1,1,1],[1,1,1],[1,1,1]], 1, 1,2
        Output= [[2,2,2],[2,1,2],[2,2,2]]
        self.assertEqual(Output, get_sol().colorBorder(grid,row,col,color))
    def test_4(self):
        grid,row,col,color= [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]], 2, 2,2
        Output= [[2,2,2,2],[2,1,1,2],[2,1,1,2],[2,2,2,2]]
        self.assertEqual(Output, get_sol().colorBorder(grid,row,col,color))
    def test_5(self):
        grid,row,col,color= [[1,2,1,2,1,2],[2,2,2,2,1,2],[1,2,2,2,1,2]], 1, 3, 1
        Output= [[1,1,1,1,1,2],[1,2,1,1,1,2],[1,1,1,1,1,2]]
        self.assertEqual(Output, get_sol().colorBorder(grid,row,col,color))
    # def test_6(self):
