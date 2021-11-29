import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/redundant-connection-ii/discuss/108070/Python-O(N)-concise-solution-with-detailed-explanation-passed-updated-testcases
    def findRedundantDirectedConnection(self, edges:List[List[int]])->List[int]:
        def union( a, b):
            parent[find(b)] = find(a)
        def find(a):
            if parent[a]!=a:
                parent[a]=find(parent[a])
            return parent[a]

        def detectCycle(u,vis=set()): # u is a node
            vis.add(u)
            for v in g[u]:
                if v in vis: return [u,v]
                return detectCycle(v,vis)

        n=len(edges)
        parent = [i for i in range(n+1)] # union parent
        g = defaultdict(list)
        hasParent = [False] * (n + 1) # Whether a vertex has already got a parent
        criticalEdge = None

        for u,v in edges:
            g[u].append(v)
            if hasParent[v]: # already has parent. u is the second parent
                criticalEdge = [u, v]  # If a vertex has more than one parent, record the last edge
            hasParent[v] = True
            if find(u) == find(v): # If a loop is found, record the edge that occurs last
                cycleEdge = [u, v]
            union(u, v)

        if not criticalEdge:   # Case 1
            return cycleEdge
        ret=detectCycle(criticalEdge[1])
        return ret if ret else criticalEdge # case 2 and case 3

class MyTestCase(unittest.TestCase):
    def test_1(self):
        actual = get_sol().findRedundantDirectedConnection(edges = [[1,2],[1,3],[2,3]])
        expected = [2,3]
        self.assertEqual(expected, actual)
    def test_2(self):
        actual = get_sol().findRedundantDirectedConnection(edges=[[1,2],[2,3],[3,4],[4,1],[1,5]])
        expected = [4,1]
        self.assertEqual(expected, actual)
    def test_3(self):
        actual = get_sol().findRedundantDirectedConnection(edges=[[1,4],[4,2],[2,1],[3,1]])
        expected = [2,1]
        self.assertEqual(expected, actual)
