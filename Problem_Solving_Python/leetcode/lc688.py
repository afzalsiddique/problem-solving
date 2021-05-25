import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp={}
        dir = [(-2,-1), (-2,1), (2,-1), (2,1), (-1,-2), (1,-2), (-1,2), (1,2)]
        def backtrack(k,row,col):
            if not 0<=row<n or not 0<=col<n: return 0
            if k==0: return 1
            if (k,row,col) in dp: return dp[(k,row,col)]
            probab=0
            for dr,dc in dir:
                probab+= 1/8 * backtrack(k-1,row+dr,col+dc)
            dp[(k,row,col)] = probab
            return probab

        return backtrack(k,row,column)

class tester(unittest.TestCase):
    def test01(self):
        n = 3
        k = 2
        row = 0
        column = 0
        Output= 0.06250
        self.assertEqual(Output, get_sol().knightProbability(n, k, row, column))
    def test02(self):
        n = 1
        k = 0
        row = 0
        column = 0
        Output= 1.00000
        self.assertEqual(Output, get_sol().knightProbability(n, k, row, column))
    def test03(self):
        n = 8
        k = 30
        row = 6
        column = 4
        Output= 0.00019
        self.assertEqual(Output, get_sol().knightProbability(n, k, row, column))
