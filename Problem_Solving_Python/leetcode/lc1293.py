import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
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


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(6, get_sol().shortestPath(grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1))
    def test2(self):
        self.assertEqual(-1, get_sol().shortestPath(grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1))
    def test3(self):
        self.assertEqual(14, get_sol().shortestPath([[0,0],[1,0],[1,0],[1,0],[1,0],[1,0],[0,0],[0,1],[0,1],[0,1],[0,0],[1,0],[1,0],[0,0]], 4))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
