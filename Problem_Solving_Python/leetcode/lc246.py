from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; import functools
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        q=deque()
        q.append((start[0],start[1]))
        m,n=len(grid),len(grid[0])
        vis=set()
        pq=[]
        dist=0
        while q:
            for _ in range(len(q)):
                x,y=q.popleft()
                if not 0<=x<m or not 0<=y<n:
                    continue
                if grid[x][y]==0:
                    continue
                if (x,y) in vis:
                    continue
                vis.add((x,y))
                if pricing[0]<=grid[x][y]<=pricing[1]:
                    heappush(pq,(-dist,-grid[x][y],-x,-y))
                    if len(pq)>k:
                        heappop(pq)
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    newX,newY=x+dx,y+dy
                    q.append((newX,newY))
            dist+=1
        res=[]
        while pq:
            _,_,x,y=heappop(pq)
            res.append([-x,-y])
        return res[::-1]

class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual([[0,1],[1,1],[2,1]],get_sol().highestRankedKItems(grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]], pricing = [2,5], start = [0,0], k = 3))
    def test02(self):
        self.assertEqual([[2,1],[1,2]],get_sol().highestRankedKItems(grid = [[1,2,0,1],[1,3,3,1],[0,2,5,1]], pricing = [2,3], start = [2,3], k = 2))
    def test03(self):
        self.assertEqual([[2,1],[2,0]],get_sol().highestRankedKItems(grid = [[1,1,1],[0,0,1],[2,3,4]], pricing = [2,3], start = [0,0], k = 3))
    # def test04(self):
    # def test05(self):
