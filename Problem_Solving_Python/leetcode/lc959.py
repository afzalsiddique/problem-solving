import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # dfs
    # https://leetcode.com/problems/regions-cut-by-slashes/discuss/205674/DFS-on-upscaled-grid
    def regionsBySlashes(self, grid: List[str]) -> int:
        m,n=len(grid),len(grid[0])
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        new_grid=[['.']*(n*3) for _ in range(m*3)]
        vis=set()
        def draw_slash(x, y):
            new_x,new_y = x * 3, y * 3
            if grid[x][y]== '/':
                for i in range(3):
                    new_grid[new_x+i][new_y+2-i]='1'
            elif grid[x][y]=='\\':
                for i in range(3):
                    new_grid[new_x+i][new_y+i]='1'
        def dfs(x,y):
            if not 0<=x<len(new_grid) or not 0<=y<len(new_grid[0]): return False
            if new_grid[x][y]=='1': return False
            if (x,y) in vis: return False
            vis.add((x,y))
            for dx,dy in dirs:
                dfs(x+dx,y+dy)
            return True

        for i in range(m):
            for j in range(n):
                draw_slash(i,j)
        # for x in new_grid: print(''.join(x))

        res=0
        for i in range(len(new_grid)):
            for j in range(len(new_grid[0])):
                res+=dfs(i,j)
        return res



class tester(unittest.TestCase):
    def test_1(self):
        grid = [" /","/ "]
        Output= 2
        self.assertEqual(Output, get_sol().regionsBySlashes(grid))
    def test_2(self):
        grid = [" /","  "]
        Output= 1
        self.assertEqual(Output, get_sol().regionsBySlashes(grid))
    def test_3(self):
        grid = ["\\/","/\\"]
        Output= 4
        self.assertEqual(Output, get_sol().regionsBySlashes(grid))
    def test_4(self):
        grid = ["/\\","\\/"]
        Output= 5
        self.assertEqual(Output, get_sol().regionsBySlashes(grid))
    def test_5(self):
        grid = ["//","/ "]
        Output= 3
        self.assertEqual(Output, get_sol().regionsBySlashes(grid))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):

