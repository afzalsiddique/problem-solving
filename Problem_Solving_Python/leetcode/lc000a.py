import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def countPoints(self, rings: str) -> int:
        n=len(rings)
        i=0
        arr=[set() for _ in range(10)]
        while i<n:
            arr[int(rings[i+1])].add(rings[i])
            i+=2
        return sum([True for x in arr if len(x)==3])



class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(0, get_sol().minRefuelStops(target = 1, startFuel = 1, stations = []))
    def test2(self):
        self.assertEqual(-1, get_sol().minRefuelStops(target = 100, startFuel = 1, stations = [[10,100]]))
    def test3(self):
        self.assertEqual(2, get_sol().minRefuelStops(target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
