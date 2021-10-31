import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/valid-square/discuss/103442/C++-3-lines-(unordered_set)/106589
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(a,b):
            x = b[0]-a[0]
            y = b[1]-a[1]
            return x*x+y*y

        sett = set() # should contain two distances. diagonal and side length
        sett.add(distance(p1,p2))
        sett.add(distance(p1,p3))
        sett.add(distance(p1,p4))
        sett.add(distance(p2,p3))
        sett.add(distance(p2,p4))
        sett.add(distance(p3,p4))
        if 0 in sett: return False # if it contains 0, then quadrilateral can't be formed
        return len(sett)==2

class Solution2:
    #  a                        d
    #   _________________________
    #   |                       |
    #   |                       |
    #   |                       |
    #   |_______________________|
    #   c                       b
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(a,b):
            x = b[0]-a[0]
            y = b[1]-a[1]
            return x*x+y*y

        points = [p1,p2,p3,p4]
        points = [(x,y) for x,y in points]
        sett = set(tuple(points))
        if len(sett)<4: return False # two points are the same
        a = points[0]
        for i in range(1,4):
            b = points[i]
            c, d = [p for p in points if p != b and p != a]
            if distance(a,b)==distance(c,d): # rectangle. because diagonals are same. not true for all cases. check test case 6
                if distance(a,c)==distance(a,d)==distance(b,c)==distance(b,d): # rhombus
                    return True # rectangle and rhombus == square
        return False


class MyTestCase(unittest.TestCase):
    def test1(self):
        p1,p2,p3,p4 = [0,0],  [1,1],  [1,0],  [0,1]
        Output= True
        self.assertEqual(Output, get_sol().validSquare(p1,p2,p3,p4))
    def test2(self):
        p1,p2,p3,p4 = [0,0],  [1,1],  [1,0],  [0,12]
        Output= False
        self.assertEqual(Output, get_sol().validSquare(p1,p2,p3,p4))
    def test3(self):
        p1,p2,p3,p4 = [1,0],  [-1,0],  [0,1],  [0,-1]
        Output= True
        self.assertEqual(Output, get_sol().validSquare(p1,p2,p3,p4))
    def test4(self):
        p1,p2,p3,p4 = [0,0], [5,0], [5,4], [0,4]
        Output= False
        self.assertEqual(Output, get_sol().validSquare(p1,p2,p3,p4))
    def test5(self):
        p1,p2,p3,p4 = [0,0], [1,1], [1,0], [1,1]
        Output= False
        self.assertEqual(Output, get_sol().validSquare(p1,p2,p3,p4))
    def test6(self):
        p1,p2,p3,p4 = [2,1], [2,2], [2,0], [0,1]
        Output= False
        self.assertEqual(Output, get_sol().validSquare(p1,p2,p3,p4))
    def test7(self):
        p1,p2,p3,p4 = [1,1], [5,3], [3,5], [7,7]
        Output= False
        self.assertEqual(Output, get_sol().validSquare(p1,p2,p3,p4))
    def test8(self):
        p1,p2,p3,p4 = [0,0], [0,2], [-1,math.sqrt(3)], [1,math.sqrt(3)]
        Output= False
        self.assertEqual(Output, get_sol().validSquare(p1,p2,p3,p4))