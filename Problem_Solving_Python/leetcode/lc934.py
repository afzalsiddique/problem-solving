import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    dir = [(0,1),(0,-1),(1,0),(-1,0)]
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def initialize_island(i,j,island): # dfs
            if not 0<=i<m or not 0<=j<n: return
            if grid[i][j]==0: return
            if (i,j) in island: return
            island.add((i, j))
            for di,dj in self.dir:
                initialize_island(i+di,j+dj,island)

        island1,island2 = set(),set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and not island1:
                    initialize_island(i,j,island1)
                    continue
                if grid[i][j]==1 and (i,j) not in island1:
                    initialize_island(i,j,island2)

        # if island1.intersection(island2): print('not okay')
        vis=set()
        q = deque(island1)
        ans=0
        while q:
            for _ in range(len(q)):
                x,y = q.popleft()
                if (x,y) in island2: return ans-1
                if (x,y) in vis: continue
                vis.add((x,y))
                for dx,dy in self.dir:
                    new_x=x+dx
                    new_y = y+dy
                    if 0<=new_x<m and 0<=new_y<n: q.append((new_x,new_y))
            ans+=1
class tester(unittest.TestCase):
    def test01(self):
        grid = [[0,1],[1,0]]
        Output= 1
        self.assertEqual(Output,get_sol().shortestBridge(grid))
    def test02(self):
        grid = [[0,1,0],[0,0,0],[0,0,1]]
        Output= 2
        self.assertEqual(Output,get_sol().shortestBridge(grid))
    def test03(self):
        grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
        Output= 1
        self.assertEqual(Output,get_sol().shortestBridge(grid))
    def test04(self):
        grid = [[1,1,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
        Output= 3
        self.assertEqual(Output,get_sol().shortestBridge(grid))
