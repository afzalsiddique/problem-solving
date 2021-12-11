import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
# there is only one path from target to start
class Solution:
    # tle
    def reachingPoints(self, i: int, j: int, x: int, y: int) -> bool:
        if i>x or j>y: return False
        while x>i and y>j:
            if x < y:
                y -= x
            else:
                x -= y

        if x==i:
            while y>j:
                y-=i
            if y==j: return True
        if y==j:
            while x>i:
                x-=j
            if x==i: return True
        return False
class Solution2:
    def reachingPoints(self, i: int, j: int, x: int, y: int) -> bool:
        if i>x or j>y: return False
        while x>i and y>j:
            if x < y:
                y %= x
            else:
                x %= y

        if x == i and (y - j) % i == 0:
            return True

        return y == j and (x - i) % y == 0


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, get_sol().reachingPoints(i= 1, j= 1, x= 3, y= 5))
    def test2(self):
        self.assertEqual(False, get_sol().reachingPoints(i= 1, j= 1, x= 2, y= 2))
    def test3(self):
        self.assertEqual(True, get_sol().reachingPoints(i= 1, j= 1, x= 1, y= 1))
    def test4(self):
        self.assertEqual(False, get_sol().reachingPoints(35, 13, 455955547, 420098884))
    def test5(self):
        self.assertEqual(True, get_sol().reachingPoints(9, 10, 9, 19))
    def test6(self):
        self.assertEqual(True, get_sol().reachingPoints(3, 3, 12, 9))
    def test7(self):
        self.assertEqual(False, get_sol().reachingPoints(2, 4, 15, 9))
    def test8(self):
        self.assertEqual(False, get_sol().reachingPoints(10, 4, 10, 20))
    def test9(self):
        self.assertEqual(False, get_sol().reachingPoints(3, 7, 3, 4))
    def test10(self):
        self.assertEqual(False, get_sol().reachingPoints(2, 2, 1000000000, 4))
