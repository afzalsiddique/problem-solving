import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD=10**9+7
        speed,efficiency=zip(*sorted(zip(speed,efficiency),key=lambda x:-x[1]))
        pq=[]
        summ=0
        res=float('-inf')
        for i in range(n):
            s,e=speed[i],efficiency[i]

            heappush(pq,s)
            summ+=s
            if len(pq)>k:
                summ-=heappop(pq)
            res=max(res,summ*e)
        return res % MOD

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(60, get_sol().maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2))
    def test2(self):
        self.assertEqual(68, get_sol().maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3))
    def test3(self):
        self.assertEqual(72, get_sol().maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4))
    def test4(self):
        self.assertEqual(56, get_sol().maxPerformance(3, [2,8,2], [2,7,1], 2))
    def test5(self):
        self.assertEqual(98, get_sol().maxPerformance(7, [1,4,1,9,4,4,4], [8,2,1,7,1,8,4], 6))
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):
