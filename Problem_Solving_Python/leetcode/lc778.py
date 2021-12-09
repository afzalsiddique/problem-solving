import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
def get_sol(): return Solution()
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        vis=set()
        heap = [(grid[0][0],0,0)] # (time,i,j)
        t=0
        while heap:
            while heap and heap[0][0]==t:
                maxx,i,j=heappop(heap)
                if (i,j) in vis: continue
                vis.add((i,j))
                if i==n-1 and j==n-1:
                    return max(maxx,grid[i][j])
                for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                    new_i,new_j=i+di,j+dj
                    if not 0<=new_i<n or not 0<=new_j<n: continue
                    tmp=max(maxx,grid[new_i][new_j])
                    heappush(heap,(tmp,new_i,new_j))
            t+=1
class Solution2:
    # optimized
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        vis=set()
        vis.add((0,0))
        heap = [(grid[0][0],0,0)] # (time,i,j)
        t=0
        while heap:
            while heap and heap[0][0]==t:
                maxx,i,j=heappop(heap)
                if i==n-1 and j==n-1:
                    return max(maxx,grid[i][j])
                for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                    new_i,new_j=i+di,j+dj
                    if not 0<=new_i<n or not 0<=new_j<n: continue
                    if (new_i,new_j) in vis: continue
                    vis.add((new_i,new_j))
                    tmp=max(maxx,grid[new_i][new_j])
                    heappush(heap,(tmp,new_i,new_j))
            t+=1
class Solution3:
    # tle
    def swimInWater(self, grid: List[List[int]]) -> int:
        def dfs(i,j,maxx):
            if not 0<=i<n or not 0<=j<n: return float('inf')
            if (i,j) in vis: return float('inf')
            vis.add((i,j))
            if i==n-1 and j==n-1:
                vis.remove((i,j))
                return max(maxx,grid[i][j])
            ans=float('inf')
            for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ans=min(ans,dfs(i+di,j+dj,max(maxx,grid[i][j])))
            vis.remove((i,j))
            return ans

        n=len(grid)
        vis=set()
        return dfs(0,0,grid[0][0])

class tester(unittest.TestCase):
    def test1(self):
        Output= 3
        self.assertEqual(Output,get_sol().swimInWater(grid = [[0,2],[1,3]]))
    def test2(self):
        Output= 16
        self.assertEqual(Output,get_sol().swimInWater(grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))
    def test3(self):
        Output= 35
        self.assertEqual(Output,get_sol().swimInWater(grid = [[35,19,17,25,4,10],[8,18,29,21,28,31],[15,5,33,2,13,3],[26,20,27,23,11,1],[6,14,24,7,12,16],[30,34,32,22,0,9]]))
    # def test4(self):
    #     self.assertEqual(Output,get_sol().numSimilarGroups(n = 1, k = 2))
    # def test5(self):