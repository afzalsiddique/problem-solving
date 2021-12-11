import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # not finished
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        def func(pos, fuel, li):
            if pos>=target: return 0
            new_li= li[:]
            minn=float('inf')
            while li and fuel>=new_li[0][1]:
                new_fuel=fuel-new_li[0]+new_li[0][1]
                new_li.popleft()
                minn=min(minn,func(new_li[0][0],new_fuel,new_li[:]))
            return minn


        stations.sort()
        stations=deque(stations)
        return func(0,startFuel,stations)


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, get_sol().minRefuelStops(k = 1, n = 2))
    # def test2(self):
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
