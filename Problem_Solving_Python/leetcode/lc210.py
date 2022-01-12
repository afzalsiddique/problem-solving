import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=ddTC4Zovtbc
    # topological sort
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        NOT_VISITED=0; VISITED=1; PROCESSING=-1
        visited = [NOT_VISITED for _ in range(numCourses)]
        res=[]
        g=defaultdict(list)
        for x,y in prerequisites: g[y].append(x)
        def dfs(u):
            if visited[u]==PROCESSING: # loop found
                return False
            if visited[u]==VISITED: return True
            visited[u]=PROCESSING
            for v in g[u]:
                if not dfs(v): return False
            visited[u]=VISITED
            res.append(u)
            return True

        for u in range(numCourses):
            if not dfs(u): return []
        return res[::-1]


class Tester(unittest.TestCase):
    def test_1(self):
        self.assertEqual([0,1],get_sol().findOrder(2,[[1,0]]))
    def test_2(self):
        self.assertIn(get_sol().findOrder(4,[[1,0],[2,0],[3,1],[3,2]]),[[0,1,2,3],[0,2,1,3]])
    def test_3(self):
        self.assertEqual([0],get_sol().findOrder(1,[]))
    def test_4(self):
        self.assertEqual([],get_sol().findOrder(2,[[0,1],[1,0]]))
