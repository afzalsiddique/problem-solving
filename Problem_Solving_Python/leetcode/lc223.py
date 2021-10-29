import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    #                      (ax2,ay2)
    #   _________________________
    #   |                       |
    #   |                       |
    #   |                       |
    #   _________________________
    #   (ax1,ay1)
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        area1 = abs(ax2 - ax1) * abs(ay1 - ay2)
        area2 = abs(bx1 - bx2) * abs(by1 - by2)
        w = min(ax2, bx2) - max(ax1, bx1)
        h = min(ay2, by2) - max(ay1, by1)
        if w<=0 or h<=0:
            return area1 + area2
        else:
            return area1 + area2 - w*h

class MyTestCase(unittest.TestCase):
    def test1(self):
        ax1,ay1,ax2,ay2,bx1,by1,bx2,by2 = -3,  0,  3,  4,  0,  -1,  9,  2
        Output= 45
        self.assertEqual(Output, get_sol().computeArea(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2))
    def test2(self):
        ax1,ay1,ax2,ay2,bx1,by1,bx2,by2 = -2, -2, 2, 2, -2, -2, 2, 2
        Output= 16
        self.assertEqual(Output, get_sol().computeArea(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
