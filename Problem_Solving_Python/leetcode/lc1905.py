import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        WATER,LAND=0,1
        def dfs(i,j):
            if (i,j) in vis: return True
            vis.add((i,j))
            grid2[i][j]=WATER # make this cell water to avoid coming to the same island multiple times
            ans = True
            if grid1[i][j]==WATER:
                ans = False # do not return immediately
            for (di,dj) in [(1,0),(0,1),(-1,0),(0,-1)]:
                x,y = i+di,j+dj
                if not 0<=x<m or not 0<=y<n or grid2[x][y]==WATER: continue
                tmp = dfs(x,y) # do not return immediately if is False
                ans &= tmp
            return ans




        m,n=len(grid1),len(grid1[0])
        vis = set()
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j]==LAND:
                    cnt += dfs(i,j)
        return cnt


class MyTestCase(unittest.TestCase):
    def test1(self):
        grid1,grid2 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],  [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
        self.assertEqual(3, get_sol().countSubIslands(grid1,grid2))
    def test2(self):
        grid1,grid2 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],  [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
        self.assertEqual(2, get_sol().countSubIslands(grid1,grid2))
    def test3(self):
        grid1,grid2 = [[1,1,1,1,1],[1,0,1,0,1]],  [[0,1,0,1,0],[1,0,0,0,1]]
        self.assertEqual(4, get_sol().countSubIslands(grid1,grid2))
    def test4(self):
        grid1,grid2 = [[1,0,0,0,0],[1,1,0,1,1]],  [[1,0,1,1,0],[0,1,0,1,0]]
        self.assertEqual(2, get_sol().countSubIslands(grid1,grid2))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
