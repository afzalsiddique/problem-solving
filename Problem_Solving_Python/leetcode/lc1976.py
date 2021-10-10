import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        g=defaultdict(list)
        for u,v,w in roads:
            g[u].append((v,w))
            g[v].append((u,w))
        dist = [float('inf')]*n
        dist[0]=0
        pq = [(0,0)]
        ways = [0]*n
        ways[0] = 1
        while pq:
            d,u = heappop(pq)
            if dist[u]<d: continue
            for v,w in g[u]:
                if d+w<dist[v]:
                    dist[v]=d+w
                    ways[v] = ways[u]
                    heappush(pq,(d+w,v))
                elif d+w==dist[v]:
                    ways[v]+=ways[u]
        return ways[-1]%(10**9+7)

class MyTestCase(unittest.TestCase):
    def test1(self):
        n,roads = 7,  [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
        Output= 4
        self.assertEqual(Output, get_sol().countPaths(n,roads))
    def test2(self):
        n,roads = 2,  [[1,0,10]]
        Output= 1
        self.assertEqual(Output, get_sol().countPaths(n,roads))
    # def test3(self):
    # def test4(self):
