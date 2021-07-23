import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # union find
    def equationsPossible(self, equations: List[str]) -> bool:
        root = {}
        def add(x):
            if x not in root:
                root[x] = x
        def find(x):
            if x not in root:
                p = x
            else:
                p = root[x]
            if p==x:
                return p
            root[x] = find(root[x])
            return root[x]
        def union(x,y):
            add(x),add(y)
            px,py = find(x), find(y)
            root[px]=root[py]

        # if x==y then x and y will belong to the same component
        for eq in equations:
            if eq[1]=='=':
                union(eq[0],eq[3])

        # if x!=y then x and y will belong the different components
        for eq in equations:
            if eq[1]=='!':
                px, py = find(eq[0]), find(eq[3])
                if px==py:
                    return False
        return True
class Solution2:
    # graph coloring and dfs
    def equationsPossible(self, equations: List[str]) -> bool:
        colors={}
        def dfs(u,color):
            if u in colors: return
            colors[u]=color
            for v in g[u]:
                dfs(v,color)
        g=defaultdict(set)
        for a,sign,__,b in equations:
            if sign=='=':
                g[a].add(b)
                g[b].add(a)

        color=0
        for a,sign,__,b in equations:
            if sign=='=':
                if a not in colors:
                    dfs(a,color)
                    color+=1
                elif b not in colors:
                    dfs(b,color)
                    color+=1
        for a,sign,__,b in equations:
            if sign=='!':
                if a==b: return False
                if a not in colors or b not in colors:
                    continue
                if colors[a]==colors[b]: return False
        return True

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(False, get_sol().equationsPossible(["a==b","b!=a"]))
    def test_2(self):
        self.assertEqual(True, get_sol().equationsPossible(["b==a","a==b"]))
    def test_3(self):
        self.assertEqual(True, get_sol().equationsPossible(["a==b","b==c","a==c"]))
    def test_4(self):
        self.assertEqual(False, get_sol().equationsPossible(["a==b","b!=c","c==a"]))
    def test_5(self):
        self.assertEqual(True, get_sol().equationsPossible(["c==c","b==d","x!=z"]))
    def test_6(self):
        self.assertEqual(False, get_sol().equationsPossible(["a!=a"]))
    def test_7(self):
        self.assertEqual(False, get_sol().equationsPossible(["a==b","e==c","b==c","a!=e"]))
    def test_8(self):
        self.assertEqual(True, get_sol().equationsPossible(["b==a","a==b"]))
