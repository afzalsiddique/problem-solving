from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution()
# class Solution:
    # try union find approach as well
    # def latestDayToCross(self, m: int, n: int, cells: List[List[int]]) -> int:

class Solution:
    # bfs + binary search
    # O(mn*log(mn))
    def latestDayToCross(self, m: int, n: int, cells: List[List[int]]) -> int:
        L,W=0,1 # L=Land, W=Water
        def constructGrid(i): # construct grid for 'i' th day
            grid=[[L]*n for _ in range(m)]
            for i in range(i):
                ii,jj=cells[i]
                ii=ii-1;jj=jj-1 # 0 based
                grid[ii][jj]=W
            return grid
        def valid(day): # check if we could pass on the ith day
            grid=constructGrid(day)
            q=deque((i,j) for i in range(m) for j in range(n) if grid[i][j]==L and i==0)
            vis=set()
            while q:
                for _ in range(len(q)):
                    x,y=q.popleft()
                    if x==m-1: return True
                    if (x,y) in vis: continue
                    vis.add((x,y))
                    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                        newX,newY=x+dx,y+dy
                        if not 0<=newX<m or not 0<=newY<n: continue
                        if grid[newX][newY]==W: continue # do not jump into water
                        q.append((newX,newY))
            return False

        lo=0
        hi=min(m*n,len(cells))+1
        while lo<=hi:
            mid=(lo+hi)//2
            if valid(mid):
                lo=mid+1
            else:
                hi=mid-1
        return lo-1

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(2, get_sol().latestDayToCross(2, 2, [[1,1],[2,1],[1,2],[2,2]]))
    def test02(self):
        self.assertEqual(1, get_sol().latestDayToCross(2,  2, [[1,1],[1,2],[2,1],[2,2]]))
    def test03(self):
        self.assertEqual(3, get_sol().latestDayToCross(3, 3, [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]))
    # def test04(self):
    # def test05(self):
