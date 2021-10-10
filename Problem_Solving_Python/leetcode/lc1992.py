import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def is_farmland(i1, j1):
            if land[i1][j1]==0: return [-1, -1]
            i2,j2= i1, j1
            while i2+1<m and land[i2+1][j2]==1:
                i2+=1
            while j2+1<n and land[i1][j2 + 1]==1:
                j2+=1

            for i in range(i1,i2+1):
                for j in range(j1,j2+1):
                    land[i][j]=0
            return [i2,j2]

        m,n=len(land),len(land[0])
        res = []
        for i in range(m):
            for j in range(n):
                tmp = is_farmland(i,j)
                if tmp!=[-1,-1]:
                    res.append([i,j,tmp[0],tmp[1]])
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        land = [[1,0,0],[0,1,1],[0,1,1]]
        Output= [[0,0,0,0],[1,1,2,2]]
        self.assertEqual(Output, get_sol().findFarmland(land))
    def test2(self):
        land = [[1,1],[1,1]]
        Output= [[0,0,1,1]]
        self.assertEqual(Output, get_sol().findFarmland(land))
    def test3(self):
        land = [[0]]
        Output= []
        self.assertEqual(Output, get_sol().findFarmland(land))
    # def test4(self):
    # def test5(self):
    # def test6(self):
