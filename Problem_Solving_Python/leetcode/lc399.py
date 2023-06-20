from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution:
    # dfs
    # https://leetcode.com/problems/evaluate-division/discuss/171649/1ms-DFS-with-Explanations/289121
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(u: int, target: int, seen, val=1.0):
            if u not in graph or target not in graph:
                return -1.0
            if u in seen:
                return -1.0
            if u==target: return val
            seen.addInReverse(u)
            for v,w in graph[u]:
                res= dfs(v, target, seen, val * w)
                if res!=-1.0:
                    return res
            return -1.0

        n=len(equations)
        graph=defaultdict(list)
        for i in range(n):
            u,v =equations[i]
            value=values[i]
            graph[u].append((v,value))
            graph[v].append((u,1.0/value))

        res=[]
        for u,v in queries:
            res.append(dfs(u, v, set()))
        return res
class Solution2:
    # https://leetcode.com/problems/evaluate-division/discuss/278276/Java-Union-Find-and-DFS-Query-O(1)
    # union find
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        parents = {}
        vals = {}
        res = [0 for _ in range(len(queries))]

        def add(x):
            if x in parents: return
            parents[x] = x
            vals[x] = 1

        def find(x):
            if x in parents:
                p = parents[x]
            else:
                p = x

            if p != x:
                pp = find(p)
                vals[x] = vals[x] * vals[p]
                parents[x] = pp
            if x in parents:
                return parents[x]
            else:
                return x

        def union(x, y, value):
            add(x), add(y)
            px, py = find(x), find(y)
            parents[px] = py
            val,valsy,valsx = value, vals[y], vals[x]
            vals[px] = value * vals[y] / vals[x]

        for i in range(n):
            union(equations[i][0], equations[i][1], values[i])
        for i in range(len(queries)):
            x, y = queries[i][0], queries[i][1]
            if x in parents and y in parents and find(x) == find(y):
                res[i] = vals[x] / vals[y]
            else:
                res[i] = -1
        return res


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([6.00000, 0.50000, -1.00000, 1.00000, -1.00000], get_sol().calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
    def test02(self):
        self.assertEqual([3.0, 0.5, 20.0, 1.0, -1], get_sol().calcEquation([["a", "b"], ["a", "c"],['d','e'],['e','f'],['b','e']], [2.0, 3.0,8,7,10,13], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
