import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dfs(i1,j1,i2,j2):
            if not 0<=i1<m or not 0<=j1<n: return float('-inf')
            if not 0<=i2<m or not 0<=j2<n: return float('-inf')
            if i1==m-1:
                if i1==i2 and j1==j2: return grid[i1][j1]
                return grid[i1][j1]+grid[i2][j2]

            if (i1,j1) in vis: return float('-inf')
            if (i2,j2) in vis: return float('-inf')
            vis.add((i1,j1))
            vis.add((i2,j2))
            cnt=0
            if i1==i2 and j1==j2:
                cnt+=grid[i1][j1]
            else:
                cnt+=grid[i1][j1]
                cnt+=grid[i2][j2]
            maxx=float('-inf')
            for di1,dj1 in [(1,-1),(1,0),(1,1)]:
                for di2,dj2 in [(1,-1),(1,0),(1,1)]:
                    maxx=max(maxx,dfs(i1+di1,j1+dj1,i2+di2,j2+dj2))
            vis.discard((i1,j1))
            vis.discard((i2,j2))
            return cnt+maxx

        m,n=len(grid),len(grid[0])
        vis=set()
        return dfs(0,0,0,n-1)


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(24, get_sol().cherryPickup(grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))
    def test02(self):
        self.assertEqual(28, get_sol().cherryPickup(grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]))
    def test03(self):
        self.assertEqual(22, get_sol().cherryPickup(grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]))
    def test04(self):
        self.assertEqual(4, get_sol().cherryPickup(grid = [[1,1],[1,1]]))
    def test05(self):
        self.assertEqual(146, get_sol().cherryPickup(grid = [[8,8,10,9,1,7],[8,8,1,8,4,7],[8,6,10,3,7,7],[3,0,9,3,2,7],[6,8,9,4,2,5],[1,1,5,8,8,1],[5,6,5,2,9,9],[4,4,6,2,5,4],[4,4,5,3,1,6],[9,2,2,1,9,3]]))
    # def test06(self):
    # def test07(self):
