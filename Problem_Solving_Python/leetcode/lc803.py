from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class UnionFind:
    def __init__(self,DUMMY_CONNECTED_TO_TOP):
        self.par={}
        self.size={}
        self.DUMMY_CONNECTED_TO_TOP=DUMMY_CONNECTED_TO_TOP
    def __repr__(self): return str(self.par)
    def add(self,a:tuple[int,int]):
        if a not in self.par:
            self.par[a]=a
            self.size[a]=1
    def union(self,a:tuple[int,int],b:tuple[int,int]):
        self.add(a),self.add(b)
        a=self.find(a)
        b=self.find(b)
        if a!=b:
            if self.size[a]<self.size[b]:
                a,b=b,a
            self.par[b]=a
            self.size[a]+=self.size[b]
    def find(self,a:tuple[int,int])->tuple[int,int]:
        self.add(a)
        if a!=self.par[a]:
            self.par[a]=self.find(self.par[a])
        return self.par[a]
    def noOfBricksConnectedToTop(self):
        return self.size[self.find(self.DUMMY_CONNECTED_TO_TOP)]-1 # subtract the dummy brick
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        DUMMY_CONNECTED_TO_TOP=(-1,-1)
        def within(x:int,y:int)->bool:
            return 0<=x<len(grid) and 0<=y<len(grid[0])
        def get_4d_moves(x:int, y:int)->List[tuple[int,int]]:
            return [(x+dx,y+dy) for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)] if within(x+dx,y+dy)]
        def unionAround(i, j):
            for x,y in get_4d_moves(i,j):
                if grid[x][y] != 1: continue
                uf.union((i, j), (x, y))

            if i == 0: uf.union(DUMMY_CONNECTED_TO_TOP, (i, j))

        m,n=len(grid),len(grid[0])
        uf=UnionFind(DUMMY_CONNECTED_TO_TOP)
        for x,y in hits:
            if grid[x][y]==1:
                grid[x][y]=2 # remove the bricks which will be hit
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    unionAround(i,j) # same effect as dfs

        res=[-1]*len(hits)
        cnt=uf.noOfBricksConnectedToTop()
        for i in range(len(hits)-1,-1,-1):
            x,y=hits[i]
            if grid[x][y]==0: # does not have the brick in the first place
                res[i]=0
            else:
                grid[x][y]=1 # put back the brick which was there before the hit
                unionAround(x,y)
                newCnt=uf.noOfBricksConnectedToTop()
                res[i]=max(0,newCnt-cnt-1) # '-1' because the brick which was hit is not counted
                cnt=newCnt
        return res
class Solution2:
    # tle
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def canReachTop(i,j,vis):
            if not 0<=i<m or not 0<=j<n: return False
            if grid[i][j]==0: return False
            if (i,j) in vis: return False
            vis.add((i, j))
            if i==0: return True
            res=False
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                res=res or canReachTop(i+di,j+dj,vis)
            return res
        def remove_falling_bricks(vis:set[int]):
            for i,j in vis:
                grid[i][j]=0


        res=[]
        m,n=len(grid),len(grid[0])
        for x,y in hits:
            ans=0
            if grid[x][y]!=0:
                grid[x][y]=0
                for di,dj in [(0,1),(1,0),(-1,0),(0,-1)]:
                    vis=set()
                    if not canReachTop(x+di,y+dj,vis):
                        ans+=len(vis)
                        remove_falling_bricks(vis)
            res.append(ans)
        return res


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([2], get_sol().hitBricks(grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]))
    def test2(self):
        self.assertEqual([0,0], get_sol().hitBricks(grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]))
    def test3(self):
        self.assertEqual([1,0,1,0,0], get_sol().hitBricks([[1],[1],[1],[1],[1]], [[3,0],[4,0],[1,0],[2,0],[0,0]]))
    def test4(self):
        self.assertEqual([0,3,0], get_sol().hitBricks([[1,0,1],[1,1,1]], [[0,0],[0,2],[1,1]]))
    def test5(self):
        self.assertEqual([0,0], get_sol().hitBricks([[1,0,1],[0,0,1]], [[1,0],[0,0]]))
    def test6(self):
        self.assertEqual([0,0,1,0], get_sol().hitBricks([[1,1,1],[0,1,0],[0,0,0]], [[0,2],[2,0],[0,1],[1,2]]))
