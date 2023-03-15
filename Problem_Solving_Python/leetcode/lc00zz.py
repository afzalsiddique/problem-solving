from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        VISITED=-1
        def valid(x,y): return 0<=x<m and 0<=y<n
        def dfs(x,y,k):
            if k<0: return float('inf')
            if grid[x][y]==VISITED: return float('inf')
            if x==m-1 and y==n-1: return 0
            res=float('inf')
            val=grid[x][y]
            grid[x][y]=VISITED
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
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

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(6, get_sol().shortestPath(grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1))
    def test2(self):
        self.assertEqual(-1, get_sol().shortestPath(grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1))
    def test3(self):
        self.assertEqual(14, get_sol().shortestPath([[0,0],[1,0],[1,0],[1,0],[1,0],[1,0],[0,0],[0,1],[0,1],[0,1],[0,0],[1,0],[1,0],[0,0]], 4))
    def test4(self):
        self.assertEqual(20, get_sol().shortestPath([[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,1,1,1,1,0,0,0],[0,1,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,0,1,0],[0,0,0,0,0,0,0,0,1,0]], 1))
    def test5(self):
        self.assertEqual(8, get_sol().shortestPath([[0,0,0,0,0,0],[1,0,1,0,1,0],[1,0,0,0,1,1],[1,1,1,1,1,0]], 1))
    # def test6(self):
    # def test7(self):
