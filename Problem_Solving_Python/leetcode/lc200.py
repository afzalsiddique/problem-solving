from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
checkInput=True # check if original grid is changed after function call
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        LAND='1';WATER='0';VIS='2'
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
        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==LAND:
                    dfs(i,j)
                    res+=1
        for i in range(m): # restore the original array
            for j in range(n):
                if grid[i][j]==VIS:
                    grid[i][j]=LAND
        return res
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        ans = 0
        def dfs(x,y):
            if x>=m or y>=n or x<0 or y<0:return
            if grid[x][y]=='0':return
            grid[x][y]='0'
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(x+dx,y+dy)
            return
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    dfs(i,j)
                    ans+=1
        return ans

class Tester(unittest.TestCase):
    def test01(self):
        grid = [["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"] ]
        gridCopy=[row[:] for row in grid]
        self.assertEqual(1,get_sol().numIslands(grid))
        self.assertEqual(gridCopy if checkInput else True,grid if checkInput else True) # change if the original grid has been changed

    def test02(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        gridCopy=[row[:] for row in grid]
        self.assertEqual(3,get_sol().numIslands(grid))
        self.assertEqual(gridCopy if checkInput else True,grid if checkInput else True) # change if the original grid has been changed
    def test03(self):
        grid = [["1","1","1"],
                ["0","1","0"],
                ["0","1","0"]]
        gridCopy=[row[:] for row in grid]
        self.assertEqual(1,get_sol().numIslands(grid))
        self.assertEqual(gridCopy if checkInput else True,grid if checkInput else True) # change if the original grid has been changed

