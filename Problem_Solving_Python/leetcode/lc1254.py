import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    # https://leetcode.com/problems/number-of-closed-islands/discuss/425150/JavaC%2B%2B-with-picture-Number-of-Enclaves
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        def fill(i,j): # dfs
            if not 0<=i<m or not 0<=j<n: return
            if grid[i][j]==1: return
            grid[i][j]=1
            for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                fill(i+di,j+dj)
            return

        def dfs(i,j):
            if not 0<=i<m or not 0<=j<n: return False
            if grid[i][j]==1: return True
            grid[i][j]=1
            for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                if not dfs(i+di,j+dj): return False
            return True


        cnt=0
        for i in range(m):
            for j in [0,n-1]:
                fill(i,j)
        for i in [0,m-1]:
            for j in range(n):
                fill(i,j)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0 and dfs(i,j):
                    cnt+=1
        return cnt
class tester(unittest.TestCase):
    def test1(self):
        grid = [[1,1,1,1,1,1,1,0],
                [1,0,0,0,0,1,1,0],
                [1,0,1,0,1,1,1,0],
                [1,0,0,0,0,1,0,1],
                [1,1,1,1,1,1,1,0]]
        Output= 2
        self.assertEqual(Output,get_sol().closedIsland(grid))
    def test2(self):
        grid = [[0,0,1,0,0],
                [0,1,0,1,0],
                [0,1,1,1,0]]
        Output= 1
        self.assertEqual(Output,get_sol().closedIsland(grid))
    def test3(self):
        grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
        Output= 2
        self.assertEqual(Output,get_sol().closedIsland(grid))

    def test4(self):
        grid = [[0,0,1,1,0,1,0,0,1,0],
                [1,1,0,1,1,0,1,1,1,0],
                [1,0,1,1,1,0,0,1,1,0],
                [0,1,1,0,0,0,0,1,0,1],
                [0,0,0,0,0,0,1,1,1,0],
                [0,1,0,1,0,1,0,1,1,1],
                [1,0,1,0,1,1,0,0,0,1],
                [1,1,1,1,1,1,0,0,0,0],
                [1,1,1,0,0,1,0,1,0,1],
                [1,1,1,0,1,1,0,1,1,0]]
        Output= 5
        self.assertEqual(Output,get_sol().closedIsland(grid))
