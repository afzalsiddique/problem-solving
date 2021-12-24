import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # wrong
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD=10**9+7
        def recArea(rec):
            x1,y1,x2,y2=rec
            return abs(x1-x2)*abs(y1-y2)
        def overlapping(rec1,rec2):
            ax1,ay1,ax2,ay2=rec1
            bx1,by1,bx2,by2=rec2
            w=min(ax2,bx2)-max(ax1,bx1)
            h=min(ay2,by2)-max(ay1,by1)
            if w<=0 or h<=0:
                return 0
            return w*h
        def subtractCommon(rec1: List[int]):
            res=0
            for rec2 in li:
                res=max(res,overlapping(rec1,rec2))
            return res

        li = []
        res=0
        for i,rec in enumerate(rectangles):
            res+=recArea(rec)
            res-= subtractCommon(rec)
            li.append(rec)
            res%=MOD
        return res

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(5, get_sol().rectangleArea([[0,0,2,2],[1,0,2,3]]))
    def test2(self):
        self.assertEqual(49, get_sol().rectangleArea([[0,0,1000000000,1000000000]]))
    def test3(self):
        self.assertEqual(6, get_sol().rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]]))
    def test4(self):
        self.assertEqual(15, get_sol().rectangleArea([[0,0,3,3],[2,0,5,3]]))
    def test5(self):
        self.assertEqual(18, get_sol().rectangleArea([[0,0,3,3],[2,0,5,3],[1,1,4,4]]))
    # def test6(self):
    # def test7(self):

