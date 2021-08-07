import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        sett=set()
        for x,_ in points:
            sett.add(x)
        li = sorted(list(sett))
        maxx=0
        for i in range(len(li)-1):
            maxx=max(maxx,li[i+1]-li[i])
        return maxx

class Tester(unittest.TestCase):
    def test_1(self):
        points = [[8,7],[9,9],[7,4],[9,7]]
        Output= 1
        self.assertEqual(Output,get_sol().maxWidthOfVerticalArea(points))
    def test_2(self):
        points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
        Output= 3
        self.assertEqual(Output,get_sol().maxWidthOfVerticalArea(points))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):