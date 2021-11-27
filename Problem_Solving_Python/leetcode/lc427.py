import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def allSameVal(left,right,up,down):
            if not all(grid[i][j]==grid[up][left] for i in range(up,down+1) for j in range(left,right+1)):
                return False
            return True

        def split_ranges(l, r, u, d):
            m1 = l + (r - l + 1) // 2
            m2 = u + (d - u + 1) // 2
            return [[l, m1 - 1,u,m2-1],[m1,r,u,m2-1],[l,m1-1,m2,d],[m1,r,m2,d]]


        def split(my_range):
            left,right,up,down = my_range
            if allSameVal(left,right,up,down):
                return Node(grid[up][left], True, None,None,None,None)
            ranges = split_ranges(left,right,up,down)
            return Node(grid[up][left], False, split(ranges[0]),split(ranges[1]),split(ranges[2]),split(ranges[3]))

        n=len(grid)
        return split([0,n-1,0,n-1])


class MyTestCase(unittest.TestCase):
    def test1(self):
        grid = [[0,1],[1,0]]
        Output= [[0,1],[1,0],[1,1],[1,1],[1,0]]
        self.assertEqual(Output, get_sol().construct(grid))
    def test2(self):
        grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
        Output= [[0,1],[1,1],[0,1],[1,1],[1,0],None,None,None,None,[1,0],[1,0],[1,1],[1,1]]
        self.assertEqual(Output, get_sol().construct(grid))
    def test3(self):
        grid = [[1,1],[1,1]]
        Output= [[1,1]]
        self.assertEqual(Output, get_sol().construct(grid))
    def test4(self):
        grid = [[0]]
        Output= [[1,0]]
        self.assertEqual(Output, get_sol().construct(grid))
    def test5(self):
        grid = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
        Output= [[0,1],[1,1],[1,0],[1,0],[1,1]]
        self.assertEqual(Output, get_sol().construct(grid))
    # def test6(self):
    # def test7(self):
