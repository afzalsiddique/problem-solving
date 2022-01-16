import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD=10**9+7
        @functools.lru_cache(None)
        def dfs(i:int,fuel:int):
            if fuel<0: return 0
            res=0
            if i==finish:
                res+=1
            for j in range(n):
                if i==j: continue
                res+=dfs(j,fuel-abs(locations[i]-locations[j]))
                res%=MOD
            return res

        n=len(locations)
        return dfs(start,fuel)


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(4, get_sol().countRoutes([2,3,6,8,4],  1,  3,  5))
    def test02(self):
        self.assertEqual(5, get_sol().countRoutes( [4,3,1], 1, 0,  6))
    def test03(self):
        self.assertEqual(0, get_sol().countRoutes([5,2,1],0, 2, 3))
    def test04(self):
        self.assertEqual(615088286, get_sol().countRoutes([1,2,3], 0, 2, 40))

