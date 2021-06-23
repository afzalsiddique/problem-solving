import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution2:
    # tle
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = defaultdict(set)
        for u,v in connections:
            g[u].add(v)
            g[v].add(u)
        def one_component(u, vis): # dfs
            if u in vis: return True
            vis.add(u)
            for nei in g[u]:
                one_component(nei,vis)
            if len(vis)!=n: return False
            return True

        res = []
        for u,v in connections:
            g[u].remove(v)
            g[v].remove(u)
            if not one_component(0,set()): res.append([u,v])
            g[u].add(v)
            g[v].add(u)
        return res

class tester(unittest.TestCase):
    def test01(self):
        n = 4
        connections = [[0,1],[1,2],[2,0],[1,3]]
        Output= [[1,3]]
        self.assertEqual(Output,get_sol().criticalConnections(n,connections))