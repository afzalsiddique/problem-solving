import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
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


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, get_sol().largestIsland(grid = [[1,0],[0,1]]))
    def test2(self):
        self.assertEqual(4, get_sol().largestIsland(grid = [[1,1],[1,0]]))
    def test3(self):
        self.assertEqual(4, get_sol().largestIsland(grid = [[1,1],[1,1]]))
    def test4(self):
        self.assertEqual(1, get_sol().largestIsland(grid = [[0,0],[0,0]]))
    def test5(self):
        self.assertEqual(1, get_sol().largestIsland(grid = [[0]]))
