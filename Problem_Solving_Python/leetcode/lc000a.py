import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    def makeFancyString(self, s: str) -> str:
        n=len(s)
        l,r=0,0
        res=[]
        while r<n:
            while r<n and s[r]==s[l]:
                if r-l<2:
                    res.append(s[r])
                r+=1
            l=r
        return ''.join(res)
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
