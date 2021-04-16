from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        colors = {} # two colors are 0 and 1
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node):
            for neigh in graph[node]:
                if neigh in colors:
                    if colors[neigh] == colors[node]:return False
                else:
                    colors[neigh] = 1- colors[node]
                    if not dfs(neigh):return False
            return True

        for i in range(1,N+1):
            if i not in colors:
                colors[i]  = 1
                if not dfs(i):return False
        return True

class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().possibleBipartition(4,[[1,2],[1,3],[2,4]]))