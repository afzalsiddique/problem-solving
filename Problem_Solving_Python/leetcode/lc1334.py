from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = [[float('inf')]*n for i in range(n)]
        for i in range(n):
            g[i][i] = 0
        for u,v,w in edges:
            g[u][v] = w
            g[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    g[i][j] = min(g[i][j], g[i][k]+g[k][j])
        res_node = -1
        res_connected = float('inf')
        for i in range(n):
            conn = 0
            for j in range(n):
                if g[i][j] <= distanceThreshold:
                    conn+=1
            if conn <= res_connected:
                res_connected = conn
                res_node = i
        return res_node
class MyTestCase(unittest.TestCase):
    def test_neighbor(self):
        n = 4
        edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
        distanceThreshold = 4
        solution = Solution()
        actual = solution.findTheCity(n, edges, distanceThreshold)
        expected = 3
        self.assertEqual(expected,actual)

    def test_neighbor2(self):
        n = 5
        edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2],[2,3,1],[3,4,1]]
        distanceThreshold = 2
        solution = Solution()
        actual = solution.findTheCity(n, edges, distanceThreshold)
        expected = 0
        self.assertEqual(expected,actual)
