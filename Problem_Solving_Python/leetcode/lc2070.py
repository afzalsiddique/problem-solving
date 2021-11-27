import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x:(x[0],-x[1]))
        prices=[p[0] for p in items]
        beauty = [items[0][1]]
        for i in range(1,len(items)):
            beauty.append(max(beauty[-1],items[i][1]))
        res = []
        for q in queries:
            idx = bisect_left(prices,q)
            if idx!=len(prices) and prices[idx]==q:
                res.append(beauty[idx])
            elif prices[idx-1]<=q:
                res.append(beauty[idx-1])
            else:
                res.append(0)
        return res
class Solution22:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x:(x[0],x[1]))
        beauty = [items[0][1]]
        for i in range(1,len(items)):
            beauty.append(max(beauty[-1],items[i][1]))
        res = []
        for q in queries:
            idx = bisect_left(items,[q,float('inf')])
            if idx!=len(items) and items[idx][0]==q:
                res.append(beauty[idx])
            if items[idx-1][0]<=q:
                res.append(beauty[idx-1])
            else:
                res.append(0)
        return res
class MyTestCase(unittest.TestCase):
    def test1(self):
        items,queries = [[1,2],[3,2],[2,4],[5,6],[3,5]],  [1,2,3,4,5,6]
        Output= [2,4,5,5,6,6]
        self.assertEqual(Output, get_sol().maximumBeauty(items,queries))
    def test2(self):
        items,queries = [[1,2],[1,2],[1,3],[1,4]],  [1]
        Output= [4]
        self.assertEqual(Output, get_sol().maximumBeauty(items,queries))
    def test3(self):
        items,queries = [[10,1000]],  [5]
        Output= [0]
        self.assertEqual(Output, get_sol().maximumBeauty(items,queries))
    # def test4(self):
    # def test5(self):
    # def test6(self):
