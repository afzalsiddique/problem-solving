import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class DSU:
    def __init__(self, size: int):
        self.size = [1]*size
        self.parents = [idx for idx in range(size)]
    def __repr__(self): return str(self.parents)
    def find(self, cell) -> None:
        if self.parents[cell] != cell:
            self.parents[cell] = self.find(self.parents[cell])
        return self.parents[cell]

    def union(self, cell1, cell2) -> None:
        parent1, parent2 = self.find(cell1), self.find(cell2)

        if parent1 != parent2:
            if self.size[parent1]>self.size[parent2]:
                parent1,parent2=parent2,parent1
            self.parents[parent1] = parent2
            self.size[parent2] += self.size[parent1]

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        self.grid = grid

        self.rows, self.cols = len(grid), len(grid[0])
        ds = DSU(self.rows*self.cols+1)

        # mark hits
        for row, col in hits:
            if grid[row][col] == 1:
                grid[row][col] = 2

                # unionize bricks
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 1:
                    self.union_around(ds, row, col)

        num_bricks_left = ds.size[ds.find(0)]
        num_bricks_dropped = [0]*len(hits)

        for idx in range(len(hits)-1,-1,-1):
            row, col = hits[idx]

            if grid[row][col] == 2:
                grid[row][col] = 1
                self.union_around(ds, row, col)
                new_num_bricks_left = ds.size[ds.find(0)]
                num_bricks_dropped[idx] = max(0, new_num_bricks_left-num_bricks_left-1)
                num_bricks_left = new_num_bricks_left

        return num_bricks_dropped

    def get_pos(self, row, col):
        return (row*self.cols) + col + 1

    def union_around(self, ds, row, col):
        curr_pos = self.get_pos(row, col)
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        for delta_row, delta_col in directions:
            new_row, new_col = row+delta_row, col+delta_col

            if 0 <= new_row < self.rows and 0 <= new_col < self.cols and self.grid[new_row][new_col] == 1:
                ds.union(curr_pos, self.get_pos(new_row, new_col))

        if row == 0: ds.union(0, curr_pos)
class Solution2:
    # tle
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def canReachTop(i,j,vis):
            if not 0<=i<m or not 0<=j<n: return False
            if grid[i][j]==0: return False
            if (i,j) in vis: return False
            vis.add((i,j))
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
    # def test3(self):