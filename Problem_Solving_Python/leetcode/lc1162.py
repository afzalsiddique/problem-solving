import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # bfs
    # without vis set and changing input
    def maxDistance(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        q=deque([(i,j) for i in range(m) for j in range(n) if grid[i][j]==1])
        if len(q)==m*n or len(q)==0: return -1
        ans=0
        while q:
            ans+=1
            for _ in range(len(q)):
                i,j=q.popleft()
                for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                    x,y=i+di,j+dj
                    if 0<=x<m and 0<=y<n and grid[x][y]==0:
                        grid[x][y]=ans # grid[x][y]= anything not equal to 0
                        q.append((x,y))
        return ans-1
class Solution2:
    # bfs
    # using vis set and without changing input
    def maxDistance(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        q=deque()
        vis=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    q.append((i,j))
                    vis.add((i,j))
        ans=-1
        while q:
            for _ in range(len(q)):
                i,j=q.popleft()
                for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                    new_i,new_j=i+di,j+dj
                    if (new_i,new_j) not in vis and 0<=new_i<m and 0<=new_j<n:
                        vis.add((new_i,new_j))
                        q.append((new_i,new_j))
            ans+=1
        if ans==0 or ans==-1: return -1
        return ans
class Solution2:
    # tle
    def maxDistance(self, grid: List[List[int]]) -> int:
        def man_dist(i1,j1,i2,j2): return abs(i1-i2) + abs(j1-j2)
        m,n=len(grid),len(grid[0])
        lands=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1: lands.add((i,j))

        maxx=0
        for i in range(m):
            for j in range(n):
                minn=float('inf')
                if grid[i][j]==0:
                    for i2,j2 in lands:
                        minn=min(minn,man_dist(i,j,i2,j2))
                    maxx=max(maxx,minn)
        if maxx==float('inf') or maxx==0: return -1
        return maxx
class tester(unittest.TestCase):
    def test_1(self):
        grid = [[1,0,1],[0,0,0],[1,0,1]]
        Output= 2
        self.assertEqual(Output,get_sol().maxDistance(grid))
    def test_2(self):
        grid = [[1,0,0],[0,0,0],[0,0,0]]
        Output= 4
        self.assertEqual(Output,get_sol().maxDistance(grid))
    def test_3(self):
        grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        Output= -1
        self.assertEqual(Output,get_sol().maxDistance(grid))
    def test_4(self):
        grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
        Output= -1
        self.assertEqual(Output,get_sol().maxDistance(grid))
