import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=ddTC4Zovtbc
    # DFS topological sort
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
class Solution2:
    # bfs topological sort
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        g,incoming= defaultdict(list), [0] * n
        for u,v in prerequisites: g[v].append(u)
        for u,_ in prerequisites: incoming[u]+=1
        q=[i for i in range(n) if incoming[i]==0]
        res=[]
        courseTaken=0
        while q:
            u=q.pop()
            res.append(u)
            courseTaken+=1
            for v in g[u]:
                incoming[v]-=1
                if incoming[v]==0: q.append(v)
        return res if courseTaken==n else []


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([0,1],get_sol().findOrder(2,[[1,0]]))
    def test2(self):
        self.assertIn(get_sol().findOrder(4,[[1,0],[2,0],[3,1],[3,2]]),[[0,1,2,3],[0,2,1,3]])
    def test3(self):
        self.assertEqual([0],get_sol().findOrder(1,[]))
    def test4(self):
        self.assertEqual([],get_sol().findOrder(2,[[0,1],[1,0]]))
    def test5(self):
        self.assertEqual([],get_sol().findOrder(3, [[1,0],[1,2],[0,1]]))
