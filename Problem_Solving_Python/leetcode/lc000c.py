import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        if homePos[0]>startPos[0]:
            dir_x=1
        elif homePos[0]<startPos[0]:
            dir_x=-1
        else:
            dir_x=0

        if homePos[1]>startPos[1]:
            dir_y=1
        elif homePos[1]<startPos[1]:
            dir_y=-1
        else:
            dir_y=0

        res=0
        if dir_x!=0:
            for i in range(startPos[0],homePos[0],dir_x):
                res+=rowCosts[i+dir_x]
        if dir_y!=0:
            for i in range(startPos[1],homePos[1],dir_y):
                res+=colCosts[i+dir_y]
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        startPos,homePos,rowCosts,colCosts = [1, 0],  [2, 3],  [5, 4, 3],  [8, 2, 6, 7]
        Output= 18
        self.assertEqual(Output, get_sol().minCost(startPos,homePos,rowCosts,colCosts))
    def test2(self):
        startPos,homePos,rowCosts,colCosts = [0, 0],  [0, 0],  [5],  [26]
        Output= 0
        self.assertEqual(Output, get_sol().minCost(startPos,homePos,rowCosts,colCosts))
    def test3(self):
        startPos,homePos,rowCosts,colCosts = [2,0], [2,2], [8,5,6,12,10], [1,8,18,11,24,16]
        Output= 26
        self.assertEqual(Output, get_sol().minCost(startPos,homePos,rowCosts,colCosts))
    def test4(self):
        startPos,homePos,rowCosts,colCosts = [5,5], [5,2], [7,1,3,3,5,3,22,10,23], [5,5,6,2,0,16]
        Output= 8
        self.assertEqual(Output, get_sol().minCost(startPos,homePos,rowCosts,colCosts))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
