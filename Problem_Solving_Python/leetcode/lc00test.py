from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        VISITED=-1
        def valid(x,y): return 0<=x<m and 0<=y<n
        @cache
        def dfs(x,y,k):
            if k<0: return float('inf')
            if grid[x][y]==VISITED: return float('inf')
            if x==m-1 and y==n-1: return 0
            res=float('inf')
            val=grid[x][y]
            grid[x][y]=VISITED
            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                X,Y=x+dx,y+dy
                if not valid(X,Y): continue
                if grid[X][Y]==1:
                    res=min(res,dfs(X,Y,k-1))
                else:
                    res=min(res,dfs(X,Y,k))
            grid[x][y]=val
            return res+1

        res=dfs(0,0,k)
        return res if res!=float('inf') else -1

class Correct:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        q=deque([(0,0,0)]) # i,j,no_obstacles_broken
        vis=set()
        res=0
        while q:
            for _ in range(len(q)):
                i,j,cnt=q.popleft()
                if i==m-1 and j==n-1: return res
                if (i,j,cnt) in vis: continue
                vis.add((i,j,cnt))
                for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                    new_i,new_j=i+di,j+dj
                    if not 0<=new_i<m or not 0<=new_j<n: continue
                    if grid[new_i][new_j]==0:
                        q.append((new_i,new_j,cnt))
                    elif cnt<k:
                        q.append((new_i,new_j,cnt+1))
            res+=1
        return -1

class Tester(unittest.TestCase):
    def test01(self):
        a,b = [[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,1,1,1,1,0,0,0],[0,1,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,0,1,0],[0,0,0,0,0,0,0,0,1,0]] ,1
        self.assertEqual(Correct().shortestPath(a,b), Solution().shortestPath(a,b))
