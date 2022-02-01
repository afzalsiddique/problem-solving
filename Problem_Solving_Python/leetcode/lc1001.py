import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        def adjacentLamps(x,y):
            li=[]
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    # if not 0<=i<n or not 0<=j<n: continue # checking boundary is not necessary. because we are checking it coordinate exists in sett
                    if (i,j) in lamps:
                        li.append((i,j))
            return li

        def turnOnOrOff(a,b,cnt): # cnt==1 turnOn, cnt==-1 turnOff
            rows[a]+=cnt
            cols[b]+=cnt
            diag1[a-b]+=cnt
            diag2[a+b]+=cnt

        lamps = set(tuple(it) for it in lamps)
        rows,cols,diag1,diag2=defaultdict(int),defaultdict(int),defaultdict(int),defaultdict(int)
        for a,b in lamps:
            turnOnOrOff(a,b,1)


        res=[]
        for x,y in queries:
            flag=0
            if rows[x] or cols[y] or diag1[x-y] or diag2[x+y]: flag=1
            res.append(flag)
            for i,j in adjacentLamps(x,y):
                lamps.remove((i,j))
                turnOnOrOff(i,j,-1) # turnOff
        return res
class Solution2:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        def remove(i,j):
            for di in range(-1,2):
                for dj in range(-1,2):
                    newI=i+di
                    newJ=j+dj
                    if not 0<=newI<n or not 0<=newJ<n: continue
                    if newJ in lights[newI]:
                        diag1[newI-newJ]-=1
                        diag2[newI+newJ]-=1
                        row[newI]-=1
                        col[newJ]-=1
                        lights[newI].remove(newJ)
        def check(i,j):
            if row[i]:
                return 1
            if col[j]:
                return 1
            if diag1[i-j]:
                return 1
            if diag2[i+j]:
                return 1
            return 0

        lights=defaultdict(set)
        diag1,diag2,row,col=defaultdict(int),defaultdict(int), defaultdict(int),defaultdict(int)
        for i,j in lamps:
            if j not in lights[i]:
                diag1[i-j]+=1
                diag2[i+j]+=1
                row[i]+=1
                col[j]+=1
            lights[i].add(j)

        res=[]
        for i,j in queries:
            res.append(check(i,j) )
            remove(i,j)
        return res


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([1,0], get_sol().gridIllumination(5,[[0,0],[4,4]],[[1,1],[1,0]]))
    def test02(self):
        self.assertEqual([1,1], get_sol().gridIllumination(5,[[0,0],[4,4]], [[1,1],[1,1]]))
    def test03(self):
        self.assertEqual([1,1,0], get_sol().gridIllumination(5,[[0,0],[0,4]], [[0,4],[0,1],[1,4]]))
    def test04(self):
        self.assertEqual([1,0], get_sol().gridIllumination(5, [[0,0],[1,0]], [[1,1],[1,1]]))
    def test05(self):
        self.assertEqual([1,0,1,1,0,1], get_sol().gridIllumination(6, [[2,5],[4,2],[0,3],[0,5],[1,4],[4,2],[3,3],[1,0]], [[4,3],[3,1],[5,3],[0,5],[4,4],[3,3]]))
    def test06(self):
        self.assertEqual([0], get_sol().gridIllumination(4,[[1,0]],[[3,1]]))
    def test07(self):
        self.assertEqual([1,0], get_sol().gridIllumination(5, [[0,4]], [[0,4],[1,4]]))
    def test08(self):
        self.assertEqual([1, 0, 0, 0, 0], get_sol().gridIllumination(6, [[4,2]], [[4,3],[3,1],[5,3],[0,5],[4,4]]))
    def test09(self):
        self.assertEqual([1,1,1], get_sol().gridIllumination(5, [[0,0],[4,4]], [[1,1],[0,0],[2,2]]))
