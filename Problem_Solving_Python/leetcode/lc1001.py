import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
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
        diag1=defaultdict(int)
        diag2=defaultdict(int)
        row=defaultdict(int)
        col=defaultdict(int)
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
    def test1(self):
        self.assertEqual([1,0], get_sol().gridIllumination(5,[[0,0],[4,4]],[[1,1],[1,0]]))
    def test2(self):
        self.assertEqual([1,1], get_sol().gridIllumination(5,[[0,0],[4,4]], [[1,1],[1,1]]))
    def test3(self):
        self.assertEqual([1,1,0], get_sol().gridIllumination(5,[[0,0],[0,4]], [[0,4],[0,1],[1,4]]))
    def test4(self):
        self.assertEqual([1,0], get_sol().gridIllumination(5, [[0,0],[1,0]], [[1,1],[1,1]]))
    def test5(self):
        self.assertEqual([1,0,1,1,0,1], get_sol().gridIllumination(6, [[2,5],[4,2],[0,3],[0,5],[1,4],[4,2],[3,3],[1,0]], [[4,3],[3,1],[5,3],[0,5],[4,4],[3,3]]))
    # def test6(self):
    # def test7(self):
    # def test8(self):
