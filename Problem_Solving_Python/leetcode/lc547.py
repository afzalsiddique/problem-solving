from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def findCircleNum(self, graph: List[List[int]]) -> int:
        def dfs(u):
            res=False
            for v in range(n):
                if graph[u][v]:
                    res=True
                    graph[u][v]=0
                    graph[v][u]=0
                    dfs(v)

            return res

        n=len(graph)
        res=0
        for i in range(n):
            res+=dfs(i)
        return res
class Solution2:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = {}

        def add(x):
            if x not in parent:
                parent[x] = x

        def find(x):
            if x in parent:
                p = parent[x]
            else:
                p = x
            if p==x:
                return p

            parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            add(x),add(y)
            px,py = find(x), find(y)
            if px!=py:
                parent[px] = py

        n= len(isConnected)

        for i in range(n):
            add(i)

        for i in range(n):
            for j in range(n):
                if i==j:continue
                if isConnected[i][j]==1:
                    union(i,j)
        s = set()
        for temp_par in parent.values():
            true_parent = find(temp_par) # true_parent cannot be found until we call find function
            s.add(true_parent)
        return len(s)

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(2, get_sol().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
    def test02(self):
        self.assertEqual(3, get_sol().findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))
    def test03(self):
        self.assertEqual(1, get_sol().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
    # def test11(self):
    # def test12(self):
