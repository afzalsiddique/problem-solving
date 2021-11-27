import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(x,y,steps):
            if not 0<=x<m or not 0<=y<n: return 0
            if grid[x][y]==-1: return 0
            if grid[x][y]==2:
                if steps==total:
                    return 1
                return 0

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
        li=[[x,y] for x in range(m) for y in range(n) if grid[x][y]==1]
        start_x,start_y=li[0]
        return dfs(start_x,start_y,0)




class MyTestCase(unittest.TestCase):
    def test1(self):
        grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
        Output= 2
        self.assertEqual(Output, get_sol().uniquePathsIII(grid))
    def test2(self):
        grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
        Output= 4
        self.assertEqual(Output, get_sol().uniquePathsIII(grid))
    def test3(self):
        grid = [[0,1],[2,0]]
        Output= 0
        self.assertEqual(Output, get_sol().uniquePathsIII(grid))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
