import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n=len(plants)
        left,right=0,0
        res=0
        cap=capacity
        while right<n:
            while right<n and plants[right]<=cap:
                cap-=plants[right]
                right+=1
            res+=(left+1)+(right)+(right-left-1)
            left=right
            cap=capacity
        res-=n
        return res


class MyTestCase(unittest.TestCase):
    def test1(self):
        plants,capacity = [2,2,3,3],  5
        Output= 14
        self.assertEqual(Output, get_sol().wateringPlants(plants,capacity))
    def test2(self):
        plants,capacity = [1,1,1,4,2,3],  4
        Output= 30
        self.assertEqual(Output, get_sol().wateringPlants(plants,capacity))
    def test3(self):
        plants,capacity = [7,7,7,7,7,7,7],  8
        Output= 49
        self.assertEqual(Output, get_sol().wateringPlants(plants,capacity))
    # def test4(self):
    # def test5(self):
    # def test6(self):
