import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g=defaultdict(set)
        for u,v in roads:
            g[u].add(v)
            g[v].add(u)
        maxx=0
        for i in range(n):
            for j in range(i+1,n):
                if j in g[i]: # same as if i in g[j]
                    maxx=max(maxx,len(g[i])+len(g[j])-1)
                else:
                    maxx=max(maxx,len(g[i])+len(g[j]))
        return maxx
class Tester(unittest.TestCase):
    def test_1(self):
        n,roads = 4,[[0,1],[0,3],[1,2],[1,3]]
        Output= 4
        self.assertEqual(Output,get_sol().maximalNetworkRank(n,roads))
    def test_2(self):
        n,roads = 5,[[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
        Output= 5
        self.assertEqual(Output,get_sol().maximalNetworkRank(n,roads))
    def test_3(self):
        n,roads = 8,[[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
        Output= 5
        self.assertEqual(Output,get_sol().maximalNetworkRank(n,roads))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
