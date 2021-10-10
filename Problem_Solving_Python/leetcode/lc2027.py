import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minimumMoves(self, s: str) -> int:
        n=len(s)
        i=0
        moves=0
        while i<n:
            if s[i]=='X':
                moves+=1
                i+=3
            else:
                i+=1
        return moves


class MyTestCase(unittest.TestCase):
    def test1(self):
        s = "XXX"
        Output= 1
        self.assertEqual(Output, get_sol().minimumMoves(s))
    def test2(self):
        s = "XXOX"
        Output= 2
        self.assertEqual(Output, get_sol().minimumMoves(s))
    def test3(self):
        s="OOOO"
        Output= 0
        self.assertEqual(Output, get_sol().minimumMoves(s))
    # def test4(self):
    # def test5(self):
    # def test6(self):
