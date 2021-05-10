import itertools
import math
import operator
import random
from bisect import *
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dir = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        vis,depth = set(),0
        q=deque()
        if grid[0][0]==0: q.append((0,0))
        while q:
            depth+=1
            for _ in range(len(q)):
                i,j=q.popleft()
                if grid[i][j]!=0: continue
                if (i,j) in vis: continue
                vis.add((i,j))
                if (i,j) == (m-1,n-1): return depth
                for di,dj in dir:
                    new_i,new_j=i+di,j+dj
                    if new_i<m and new_j<n and new_i>=0 and new_j>=0:
                        q.append((new_i,new_j))
        return -1

class tester(unittest.TestCase):
    def test01(self):
        grid = [[0,1],[1,0]]
        Output= 2
        self.assertEqual(Output,get_sol().shortestPathBinaryMatrix(grid))
    def test02(self):
        grid = [[0,0,0],[1,1,0],[1,1,0]]
        Output= 4
        self.assertEqual(Output,get_sol().shortestPathBinaryMatrix(grid))
    def test03(self):
        grid = [[1,0,0],[1,1,0],[1,1,0]]
        Output= -1
        self.assertEqual(Output,get_sol().shortestPathBinaryMatrix(grid))
