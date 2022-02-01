from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

# https://www.youtube.com/watch?v=MiqoA-yF-0M
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m=len(grid)
        if not m:return 0
        n=len(grid[0])
        def dfs(x, y):
            if not 0<=x<m or not 0<=y<n: return 0
            if grid[x][y]==0: return 0
            prev_value = grid[x][y]
            grid[x][y]=0 # return 0 when visited or when there is no goal
            res=0
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                res = max(res,prev_value+dfs(x+dx,y+dy))
                # res = max(res,grid[x][y]+dfs(x+dx,y+dy)) # wrong. because we made grid[x][y]=0
            grid[x][y]=prev_value
            return res

        maxx = float('-inf')
        for i in range(m):
            for j in range(n):
                maxx=max(maxx, dfs(i,j))
        return maxx


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(24, get_sol().getMaximumGold([[0,6,0], [5,8,7], [0,9,0]]))
    def test02(self):
        self.assertEqual(28, get_sol().getMaximumGold([[1,0,7], [2,0,6], [3,4,5], [0,3,0], [9,0,20]]))
    def test03(self):
        self.assertEqual(60, get_sol().getMaximumGold([[1,0,7,0,0,0],[2,0,6,0,1,0],[3,5,6,7,4,2],[4,3,1,0,2,0],[3,0,5,0,20,0]]))
    def test04(self):
        self.assertEqual(29, get_sol().getMaximumGold([[2,0,6],[3,5,6],[4,3,1]]))
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
