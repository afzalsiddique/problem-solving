import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # for simpler sol-> https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/discuss/392940/Python-Level-by-level-BFS-solution-(similar-problems-listed)/471816
    def minimumMoves(self, grid: List[List[int]]) -> int:
        pass
class Solution2:
    # complex solution
    def minimumMoves(self, grid: List[List[int]]) -> int:
        def valid(x,y): return 0<=x<n and 0<=y<n
        def nextMoves(x1,y1,x2,y2):
            if x1==x2:
                horizontal=True
            else:
                horizontal=False
            res=[]
            if horizontal:
                newX,newY=x1+0,y1+1 # move right
                if valid(newX,newY) and grid[newX][newY]==0:
                    res.append([newX,newY,x1,y1])

                newX1,newY1=x1+1,y1+0 # move down
                newX2,newY2=x1+1,y1-1
                if valid(newX1,newY1) and valid(newX2,newY2) and grid[newX1][newY1]==0 and grid[newX2][newY2]==0:
                    res.append([newX1,newY1,newX2,newY2])

                newX1,newY1=x1+1,y1+0 # move rotate clockwise
                newX2,newY2=x1+1,y1-1
                if valid(newX1,newY1) and valid(newX2,newY2) and grid[newX1][newY1]==0 and grid[newX2][newY2]==0:
                    res.append([newX2,newY2,x2,y2])
            else:
                newX,newY=x1+1,y1+0 # move down
                if valid(newX,newY) and grid[newX][newY]==0:
                    res.append([newX,newY,x1,y1])

                newX1,newY1=x1+0,y1+1 # move right
                newX2,newY2=x1-1,y1+1
                if valid(newX1,newY1) and valid(newX2,newY2) and grid[newX1][newY1]==0 and grid[newX2][newY2]==0:
                    res.append([newX1,newY1,newX2,newY2])

                newX1,newY1=x1+0,y1+1 # rotate counter clockwise
                newX2,newY2=x1-1,y1+1
                if valid(newX1,newY1) and valid(newX2,newY2) and grid[newX1][newY1]==0 and grid[newX2][newY2]==0:
                    res.append([newX2,newY2,x2,y2])

            return res

        n=len(grid)
        start=[0,1,0,0]
        seen=set()
        res=0
        q=deque()
        q.append(start)
        while q:
            for _ in range(len(q)):
                x1,y1,x2,y2=q.popleft()
                if (x1,y1,x2,y2) in seen:
                    continue
                seen.add((x1,y1,x2,y2))
                if [x1,y1,x2,y2]==[n-1,n-1,n-1,n-2]:
                    return res
                tmp=nextMoves(x1,y1,x2,y2)
                for nxt in tmp:
                    q.append(nxt)
            res+=1
        return -1


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(11,get_sol().minimumMoves( [[0,0,0,0,0,1], [1,1,0,0,1,0], [0,0,0,0,1,1], [0,0,1,0,1,0], [0,1,1,0,0,0], [0,1,1,0,0,0]]))
    def test2(self):
        self.assertEqual(9,get_sol().minimumMoves([[0,0,1,1,1,1], [0,0,0,0,1,1], [1,1,0,0,0,1], [1,1,1,0,0,1], [1,1,1,0,0,1], [1,1,1,0,0,0]]))
    def test3(self):
        self.assertEqual(7,get_sol().minimumMoves([[0,0,1,1,1],[0,0,0,0,1],[1,1,0,0,0],[1,1,1,0,0],[1,1,1,0,0]]))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
