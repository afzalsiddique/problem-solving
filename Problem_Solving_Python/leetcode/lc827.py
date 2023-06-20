from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    # assign every cell an island_id where island_id>500
    # for every island_id store the size of that island in sizes
    # for every empty cell go in four directions and add the island_id to a set
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j, vis): # return the size of the island
            if not 0<=i<n or not 0<=j<n: return 0
            if grid[i][j]==0: return 0
            if (i,j) in vis: return 0
            vis.add((i,j))
            ans=1
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                ans += dfs(i + di, j + dj, vis)
            return ans

        n=len(grid)
        sizes=defaultdict(int)
        sizes[-1]=1
        island_id=501
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0: continue
                if grid[i][j]>500: continue # size already calculated
                vis=set()
                size=dfs(i,j,vis)
                for x,y in vis: grid[x][y]=island_id
                sizes[island_id]=size
                island_id+=1

        res=float('-inf')
        for i in range(n):
            for j in range(n):
                if grid[i][j]!=0: continue
                sett=set()
                for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                    new_i,new_j=i+di,j+dj
                    if not 0<=new_i<n or not 0<=new_j<n: continue
                    sett.add(grid[new_i][new_j])
                    ans=1
                    for island_id in sett:
                        ans+=sizes[island_id]
                    res=max(res,ans)


        # for x in grid: print(x)
        # print(sizes)
        res=max(res,max(sizes.values()))
        return res


# tle
class UnionFind:
    def __init__(self):
        self.par={}
        self.size={}
        self.parCopy={} # to save current state
        self.sizeCopy={} # to save current state
    def __repr__(self): return str(self.par)
    def add(self,a):
        if a not in self.par:
            self.par[a]=a
            self.size[a]=1
    def union(self,a,b):
        self.add(a),self.add(b)
        a=self.find(a)
        b=self.find(b)
        if a!=b:
            if self.size[a]<self.size[b]:
                a,b=b,a
            self.par[b]=a
            self.size[a]+=self.size[b]
    def find(self,a):
        self.add(a)
        if a!=self.par[a]:
            self.par[a]=self.find(self.par[a])
        return self.par[a]
    def unionAll(self,li):
        if len(li)==0: return
        if len(li)==1:
            self.add(li[0])
            return
        first=li[0]
        for second in li[1:]:
            self.union(first,second)
    def size_of_groups(self):
        for a in self.par:
            self.find(a)
        count=Counter(self.par.values())
        return list(count.values())
    def saveCurrentState(self):
        self.parCopy={k:v for k,v in self.par.items()}
        self.sizeCopy={k:v for k,v in self.size.items()}
    def restoreSavedState(self):
        self.par={k:v for k,v in self.parCopy.items()}
        self.size={k:v for k,v in self.sizeCopy.items()}
class Solution2:
    def largestIsland(self, grid: List[List[int]]) -> int:
        VISITED=2
        def within(x:int,y:int)->bool:
            return 0<=x<len(grid) and 0<=y<len(grid[0])
        def get_4d_moves(x:int, y:int)->List[tuple[int,int]]:
            return [(x+dx,y+dy) for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)] if within(x+dx,y+dy)]
        def bfs(i, j):
            if grid[i][j]!=1: return []
            q=deque()
            q.append((i, j))
            li = []
            while q:
                i, j=q.popleft()
                if grid[i][j]==VISITED: continue
                li.append((i, j))
                grid[i][j]=VISITED
                for x,y in get_4d_moves(i, j):
                    if grid[x][y]==1:
                        q.append((x,y))
            return li

        m,n=len(grid),len(grid[0])
        res=float('-inf')
        uf=UnionFind()
        for i in range(m):
            for j in range(n):
                li = bfs(i,j)
                res=max(res,len(li))
                uf.unionAll(li)

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    uf.saveCurrentState()
                    li = get_4d_moves(i,j)
                    li = [(x,y) for x,y in li if grid[x][y]==2]
                    li.append((i,j))
                    uf.unionAll(li)
                    tmp=max(uf.size_of_groups())
                    res=max(res,tmp)
                    uf.restoreSavedState()
        return res

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(3, get_sol().largestIsland(grid = [[1,0],[0,1]]))
    def test02(self):
        self.assertEqual(4, get_sol().largestIsland(grid = [[1,1],[1,0]]))
    def test03(self):
        self.assertEqual(4, get_sol().largestIsland(grid = [[1,1],[1,1]]))
    def test04(self):
        self.assertEqual(1, get_sol().largestIsland(grid = [[0,0],[0,0]]))
    def test05(self):
        self.assertEqual(1, get_sol().largestIsland(grid = [[0]]))
    def test06(self):
        self.assertEqual(326, get_sol().largestIsland(grid = [[1,1,1,0,1,0,0,0,0,1,1,1,0,1,0,1,0,1,1,0,1,0,0,0,1,0,1,0,0,1,0,0,1,1,0,0,0,1,0,1,1,1,1,0,0,0,0,1,1,0],[0,1,1,1,1,0,0,1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1,0,1,1,0,0],[1,0,1,0,0,1,0,1,1,1,1,1,1,0,1,1,1,0,0,1,1,0,0,1,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,1],[1,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1,1,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,1,1,0,1,1,1,1,1,1],[1,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,1,1,1,1,1,0,1,0,0,1,0,1,0,0,0,1,1,0,0,1,1,1,1,0,1,1,1,1,0,1,0,0,0,0],[0,1,0,0,0,0,1,0,1,1,1,1,0,0,1,1,0,0,1,1,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,0,1,1,0,1,0,0,1,1,1,1],[0,0,0,0,0,1,0,1,0,0,0,0,1,1,1,0,0,0,1,0,0,1,0,1,1,1,1,0,0,1,1,1,0,0,1,1,0,1,1,1,0,1,1,1,0,0,1,1,1,0],[0,0,1,0,0,1,1,0,0,0,0,0,1,1,0,0,1,0,1,1,1,1,1,0,1,0,0,1,0,1,1,1,1,1,0,1,0,0,1,1,0,1,0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1,0,0,1,0,1,1,0,0,1,1,0,0,1,0,0,0,0,0,1,0,0,1],[0,1,1,1,1,1,1,0,0,1,0,1,1,1,0,0,1,1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,1,1,1,1,0,1,0,0,0],[0,1,1,1,0,0,0,1,1,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,0,1,1,0,0,0,1],[0,0,0,1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,1,1,0,0,1,0,0,0,0,1,1,0,0,0,1],[0,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,0,0,0,1,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0],[1,1,1,0,1,0,1,1,1,1,1,0,0,1,0,1,1,0,1,0,1,0,0,1,1,1,0,1,0,1,0,0,1,1,1,0,0,1,0,1,1,0,1,0,1,1,0,1,0,1],[1,1,1,0,0,1,1,1,1,0,0,1,0,1,0,1,0,0,0,0,0,0,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,0,0,1,1,0,1,1,0,1,0],[1,1,0,1,0,1,1,0,0,1,0,0,1,0,1,0,0,0,0,1,1,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0,1,0,1,1,0,1,0,1,1,1,0,0],[1,0,0,1,0,1,1,0,1,1,1,0,1,1,1,0,1,0,0,1,1,1,0,1,0,0,0,1,0,1,1,0,0,0,0,1,1,1,0,0,1,0,0,0,0,1,0,1,1,0],[0,0,0,1,0,1,0,0,1,1,1,1,0,1,1,0,0,0,0,0,1,1,0,1,1,1,1,1,1,1,0,0,0,0,1,0,0,1,1,0,0,1,1,1,0,1,0,0,1,1],[1,0,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,0,0,0,1,1,1,1],[1,1,1,0,1,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,0,1,0,0,1,0,1,0,1,0,0,0,0,1,1,1,0,0,1,0,0],[1,0,0,0,1,0,0,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,0,0,1,0,0,1,1,1,0,0,1,0,1,1,1,1,1,0,0,0,1,0,0,0,1,1,1,0],[0,1,1,1,1,0,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,1,1,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0],[1,0,1,1,1,1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,1,1,1,0,0,1,0,0,1,1,1,0,1,0,1,0,1,1,1,1,0,0,1,0,1,1,1,0,1,0],[1,1,0,0,1,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,0,1,1,0,0,0,0,0,0,1,0,0,0,1,1,0,0,1,0,1,1,1,1,0,1,0,1,1],[0,1,1,1,1,1,1,0,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,1,0,1,1,0,0,0,1,0],[0,0,0,1,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,1,0,1,1,0,0,0,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,0,0,1],[1,1,0,0,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0,0,0,1,1,0,1,1,1,0,0,1,1,0,1,1,1,1,0,0,0,0,0,1,1,0,0,0,1,0,1,1],[0,1,0,1,0,1,1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,0,1,1,0,0,1,0,1,0,1,0,1,1],[0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,1,1,0,0,0,1,0,1,1,1,1,1,1,1,0,1,1,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,1],[0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,1,0,0,1,0,1,1,1,0,0,1,0,1,0,0,0,1],[1,1,0,1,0,0,0,0,1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,0,1,0,0,1,0,1,0,1,0,1],[1,0,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1,1,0,1,1,0,0,1,0,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,1,0,1,1,0,0,0,0,1,0],[0,1,0,1,1,0,1,1,1,1,0,1,1,0,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,0,1,1,0,0,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0],[1,1,1,0,1,0,1,1,0,1,0,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,0,0,1,1,1,0,1,0,0,1,1,0,1,1,0,0,0,0,1],[1,1,0,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1,1,0,0,0,1,0,1,1,0,0,0,1,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,1],[1,0,0,1,0,1,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,0,0,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1],[1,1,1,0,1,1,1,0,0,1,0,1,1,0,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,0,1,0,0,1,1,0,1,0,0,0,1,1,1,1,0,0,1,0,0,0],[1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,1,0,1,0,0,0,0,1,0,1,1,1,1],[1,0,1,0,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,0,0,0,1,0,0,1,1,1,0,0,0,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,0,0,0],[0,1,0,1,0,1,0,0,1,1,1,0,0,1,1,1,1,0,1,0,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0],[0,1,1,0,1,1,1,0,0,1,1,1,0,0,1,0,1,0,1,1,1,1,0,1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1],[0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,0,0,1,1,0,1,0,0,0,1,1,1,0,1,0,0,1,0,1,0,1,0],[0,1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,1,1,1,0,1],[1,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1],[0,0,1,0,0,1,1,0,0,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,1,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,0,0,1,0,0,1],[1,1,0,1,1,0,0,1,0,0,0,1,0,1,1,1,0,0,1,1,0,1,0,0,0,1,1,1,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,0,0,0,1,1],[0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,1,0,0,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0],[0,0,0,1,0,0,1,1,0,0,0,1,1,0,1,1,0,1,0,1,1,0,0,0,1,1,1,1,1,1,0,1,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,1,0],[0,0,0,1,0,1,0,0,1,1,1,1,1,0,0,1,0,1,0,0,0,1,1,1,0,1,1,0,1,0,1,0,0,0,0,1,1,0,1,0,1,1,0,0,0,0,0,1,1,1],[0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,0,1,1,1,1,0,1,0,1,1,0,0,1,0,1,0,0,1,0,0,0,0,1,1,1]]))
