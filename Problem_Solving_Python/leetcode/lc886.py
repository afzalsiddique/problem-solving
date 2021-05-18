from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph=defaultdict(set)
        for u,v in dislikes:
            graph[u].add(v)
            graph[v].add(u)
        colors={} # two colors are True and False
        def dfs(u):
            for v in graph[u]:
                if v in colors:
                    if colors[v]==colors[u]: return False
                else:
                    colors[v]=not colors[u]
                    if not dfs(v): return False
            return True
        for i in range(1,n+1):
            if i not in colors:
                colors[i]=True
                if not dfs(i): return False
        return True

class tester(unittest.TestCase):
    def test01(self):
        n = 3
        dislikes = [[1,2],[1,3],[2,3]]
        Output= False
        self.assertEqual(Output,get_sol().possibleBipartition(n, dislikes))
    def test02(self):
        n = 4
        dislikes = [[1,2],[1,3],[2,4]]
        Output= True
        self.assertEqual(Output,get_sol().possibleBipartition(n, dislikes))
    def test03(self):
        n = 5
        dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
        Output= False
        self.assertEqual(Output,get_sol().possibleBipartition(n, dislikes))
