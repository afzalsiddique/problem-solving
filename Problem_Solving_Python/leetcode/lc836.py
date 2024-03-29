import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        ax1,ay1,ax2,ay2=rec1
        bx1,by1,bx2,by2=rec2
        w=min(ax2,bx2)-max(ax1,bx1)
        h=min(ay2,by2)-max(ay1,by1)
        if h>0 and w>0:
            return True
        return False
class Solution2:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        ax1,ay1,ax2,ay2=rec1
        bx1,by1,bx2,by2=rec2
        w=min(ax2,bx2)-max(ax1,bx1)
        h=min(ay2,by2)-max(ay1,by1)
        if w<=0 or h<=0:
            return False
        return True

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(True, get_sol().isRectangleOverlap([0,0,2,2], [1,1,3,3]))
    def test02(self):
        self.assertEqual(False, get_sol().isRectangleOverlap([0,0,1,1], [1,0,2,1]))
    def test03(self):
        self.assertEqual(False, get_sol().isRectangleOverlap([0,0,1,1], [2,2,3,3]))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
