import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/paint-house-iii/discuss/674313/Simple-Python-explanation-and-why-I-prefer-top-down-DP-to-bottom-up
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @functools.lru_cache(None)
        def call(i,p,t): # i: houseNo, p: previous house color, t: no of neighborhood
            if t<0:
                return float('inf')
            if i==m:
                if t==0:
                    return 0
                return float('inf')

            res = float('inf')
            if houses[i]: # already colored. no need to color
                res = min(res, call(i + 1, houses[i], t - (houses[i] != p)))
            else:
                for c in range(1, n+1):
                    res = min(res, cost[i][c-1] + call(i + 1, c, t - (c != p)))
            return res

        res=call(0,'no prev color',target)
        return res if res!=float('inf') else -1
class Solution2:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @functools.lru_cache(None)
        def call(i, prevColor, t): # i: houseNo, p: previous house color, t: no of neighborhood
            if t<0:
                return float('inf')
            if i==m:
                if t==0:
                    return 0
                return float('inf')

            res = float('inf')
            if houses[i]: # already colored. no need to color
                if houses[i]==prevColor: # no neighborhood created
                    res = min(res, call(i + 1, houses[i], t))
                else:  # new neghborhood created
                    res = min(res, call(i + 1, houses[i], t-1))
            else:
                for newColor in range(1, n+1):
                    if newColor==prevColor: # no neighborhood created
                        res = min(res, cost[i][newColor-1] + call(i + 1, newColor, t))
                    else: # new neghborhood created
                        res = min(res, cost[i][newColor-1] + call(i + 1, newColor, t-1))
            return res

        res=call(0,'no prev color',target)
        return res if res!=float('inf') else -1



class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(9, get_sol().minCost(houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3))
    def test02(self):
        self.assertEqual(11, get_sol().minCost(houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3))
    def test03(self):
        self.assertEqual(-1, get_sol().minCost(houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
