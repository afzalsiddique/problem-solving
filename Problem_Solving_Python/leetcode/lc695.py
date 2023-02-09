from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        def dfs(row, col):
            if row<0 or col<0 or row>=m or col>=n:return 0
            if grid[row][col]==0:return 0
            grid[row][col]=0
            area = 1
            for (dr,dc) in [(1,0),(-1,0),(0,1),(0,-1)]:
                i,j = row + dr, col + dc
                area+= dfs(i,j)
            return area

        maxx=0
        for i in range(m):
            for j in range(n):
                maxx=max(maxx, dfs(i,j))
        return maxx

    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        def dfs(r,c):
            if grid[r][c]==0:return 0
            area = 1
            grid[r][c]=0
            for (dr,dc) in [(1,0),(-1,0),(0,1),(0,-1)]:
                i = r+dr
                j = c+dc
                if i<m and j<n and i>=0 and j >=0 and grid[i][j]==1:
                    area += dfs(i,j)
            return area

        max_area = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    area = dfs(r,c)
                    max_area=max(max_area, area)
        return max_area

## union find solution
class UnionFind:
    def __init__(self):
        self.par = {}
        self.size = {}
    def add(self,a):
        if a not in self.par:
            self.par[a]=a
            self.size[a]=1
    def find(self,a):
        self.add(a)
        if self.par[a]!=a:
            self.par[a]=self.find(self.par[a])
        return self.par[a]
    def union(self,a,b):
        self.add(a); self.add(b)
        a,b=self.find(a),self.find(b)
        if a!=b:
            if self.size[a]<self.size[b]:
                a,b=b,a
            self.size[a]+=self.size[b]
            self.par[b] = self.par[a]
    def unionAll(self,li):
        first=li[0]
        for second in iter(li[1:]):
            self.union(first,second)
    def max_size_of_groups(self):
        max_size = 0
        for x in self.par:
            x_par = self.par[x]
            max_size=max(self.size[x_par],max_size)
        return max_size

class Solution3:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def valid(i,j):
            return 0<=i<m and 0<=j<n
        def include_neigh(i,j):
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                newI,newJ=i+di,j+dj
                if valid(newI,newJ) and grid[newI][newJ]==1:
                    uf.union((i,j),(newI,newJ))

        m,n=len(grid),len(grid[0])

        uf = UnionFind()
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    uf.add((i,j))
                    include_neigh(i,j)

        return uf.max_size_of_groups()

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(6,get_sol().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
    def test02(self):
        self.assertEqual(0,get_sol().maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))
    def test03(self):
        self.assertEqual(4,get_sol().maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
    def test04(self):
        self.assertEqual(177,get_sol().maxAreaOfIsland([[1,1,0,0,1,0,1,1,1,1,1,0,0,0,1,1,0,1,0,1,1,1,1,0,0],[0,0,0,1,0,1,0,1,1,0,0,0,0,1,0,1,1,1,1,0,1,0,0,0,1],[1,0,1,0,1,1,0,0,1,1,1,0,0,0,1,0,0,1,1,1,1,1,1,0,1],[0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,1],[1,1,0,1,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,0,0,0,0,0,1],[0,1,0,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1],[1,1,1,1,0,0,0,1,0,0,1,0,0,1,0,1,1,1,1,1,0,0,0,0,0],[0,1,1,1,1,1,0,1,0,0,0,1,0,1,1,1,0,0,1,0,0,0,0,1,1],[1,1,0,0,1,1,0,1,0,1,1,0,0,0,0,1,1,1,1,0,1,1,0,0,0],[0,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,0,0,0,0,1,0,1,1,1],[0,1,1,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0],[1,0,0,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,1,1,1],[1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1],[1,1,1,0,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,1,1,0,0,1,1],[0,0,0,1,1,0,1,1,1,0,1,1,1,1,1,1,0,1,1,0,0,0,0,1,0],[0,0,1,0,0,1,0,1,1,1,1,0,1,0,0,0,1,0,1,1,1,1,1,1,1],[0,0,1,1,1,1,0,1,1,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,1],[1,0,0,1,0,1,0,0,1,1,1,1,0,0,0,1,0,1,0,1,1,1,0,1,1],[0,0,0,0,1,0,0,1,0,1,0,0,0,1,1,1,0,1,0,0,0,1,0,0,0],[1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,1,1,0,0,0,1],[1,0,0,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,1,0,1,0,1,1],[1,1,0,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,0,0,0],[1,0,0,0,0,1,1,0,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,0,0],[0,1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,0,1,1,0,1,1],[1,1,0,1,1,0,1,1,1,0,1,0,1,0,0,1,0,1,0,0,0,1,0,0,0],[0,1,0,0,1,0,0,0,0,0,0,1,0,1,1,0,1,1,0,1,1,1,0,0,0],[0,1,1,1,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1],[1,0,0,1,1,1,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0],[1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,1,1,0,1,0,0,0,0],[0,0,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,0,1,1,0],[1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,0,0,1,1,0,0,1,0,1],[0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,1,1,1,0,0,0,1,1,0,0],[0,1,0,0,1,1,0,1,1,0,1,0,1,0,0,0,0,1,1,0,0,1,1,1,1],[0,0,1,0,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,0],[1,0,1,0,1,1,0,1,1,0,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1],[1,0,1,0,1,1,1,0,1,0,1,0,1,1,0,0,1,1,0,0,1,1,0,0,1],[0,1,0,0,0,1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,1,0,1,0,1],[0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,1],[1,1,0,1,0,0,1,1,0,0,1,1,1,0,0,1,1,1,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,1,1,0,0,0,0,0],[1,0,0,0,1,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,1,0,0,0,1],[0,1,0,1,0,1,1,0,0,1,1,1,0,1,0,0,0,1,1,0,0,1,1,1,0],[1,1,1,1,0,1,0,0,1,0,1,1,0,0,1,1,0,1,0,1,0,0,1,0,1],[1,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,1,0,1,1,1,0,0,0],[1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0],[1,1,1,0,0,0,1,0,0,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,1],[0,1,1,0,1,0,0,1,0,0,0,0,1,0,1,1,1,1,1,0,1,1,1,0,1],[0,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,0,0,0,0,1,1,0,1],[0,0,1,0,1,1,0,0,1,1,1,0,1,0,0,0,1,0,1,0,1,0,1,1,0],[1,0,0,1,1,0,1,0,0,1,0,0,1,1,0,1,0,0,1,0,0,1,0,1,0]]))
    def test05(self):
        self.assertEqual(1,get_sol().maxAreaOfIsland([[1]]))

    # def test06(self):
    # def test08(self):
    # def test09(self):
