import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(x,y,steps):
            if not 0<=x<m or not 0<=y<n: return 0
            if grid[x][y]==-1: return 0
            if grid[x][y]==2: return steps==total
            if (x,y) in vis: return 0
            vis.add((x,y))

            ans=0
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                ans+=dfs(x+dx,y+dy,steps+1)
            vis.remove((x,y))
            return ans

        m,n= len(grid), len(grid[0])
        total=sum(grid[x][y]==0 for x in range(m) for y in range(n))+1
        vis=set()
        start_li=[[x,y] for x in range(m) for y in range(n) if grid[x][y]==1]
        start_x,start_y=start_li[0]
        return dfs(start_x,start_y,0)


class Solution2:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def within(x,y): return 0<=x<m and 0<=y<n
        def get_moves(x,y): return [(x+dx,y+dy) for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)] if within(x+dx,y+dy)]
        def get_start_or_finish(a):
            for x in range(m):
                for y in range(n):
                    if grid[x][y]==a:
                        return [x,y]
        def get_finish(): return get_start_or_finish(2)
        def get_start(): return get_start_or_finish(1)
        def allVisited():
            return all(grid[i][j]!=0 for i in range(m) for j in range(n))
        def dfs(x,y):
            if [x,y]==FINISH:
                return allVisited()
            if grid[x][y]==-1:
                return 0
            if grid[x][y]==VISITED:
                return 0
            grid[x][y]=VISITED
            res=0
            for X,Y in get_moves(x,y):
                res+=dfs(X,Y)
            grid[x][y]=0
            return res

        VISITED=3
        m,n=len(grid),len(grid[0])
        START,FINISH=get_start(),get_finish()
        x,y=START
        grid[x][y]=0
        return dfs(x,y)


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, get_sol().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
    def test2(self):
        self.assertEqual(4, get_sol().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
    def test3(self):
        self.assertEqual(0,get_sol().uniquePathsIII([[0,1],[2,0]]))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
