import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/spiral-matrix-iii/discuss/158970/C%2B%2BJavaPython-112233-Steps
    def spiralMatrixIII(self, R, C, x, y):
        def turn_right(dx,dy): return dy,-dx
        res = []
        dx, dy= 0, 1
        n=2
        while len(res) < R * C:
            bound=n//2
            for i in range(bound):
                if 0 <= x < R and 0 <= y < C:
                    res.append([x, y])
                x, y = x + dx, y + dy
            dx,dy=turn_right(dx,dy)
            n+=1
        return res
class Solution2:
    def spiralMatrixIII(self, R: int, C: int, r: int, c: int) -> List[List[int]]:
        res=[]
        cnt=1
        res.append([r,c])
        while len(res)<R*C:
            for j in range(cnt): # right
                c+=1
                if 0<=r<R and 0<=c<C: res.append([r,c])
            for i in range(cnt): # down
                r+=1
                if 0<=r<R and 0<=c<C: res.append([r,c])
            cnt+=1
            for j in range(cnt): # left
                c-=1
                if 0<=r<R and 0<=c<C: res.append([r,c])
            for i in range(cnt): # up
                r-=1
                if 0<=r<R and 0<=c<C: res.append([r,c])
            cnt+=1
        return res


class tester(unittest.TestCase):
    def test_1(self):
        rows = 1
        cols = 4
        rStart = 0
        cStart = 0
        Output= [[0,0],[0,1],[0,2],[0,3]]
        self.assertEqual(Output, get_sol().spiralMatrixIII(rows,cols,rStart,cStart))
    def test_2(self):
        rows = 5
        cols = 6
        rStart = 1
        cStart = 4
        Output= [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
        self.assertEqual(Output, get_sol().spiralMatrixIII(rows,cols,rStart,cStart))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
