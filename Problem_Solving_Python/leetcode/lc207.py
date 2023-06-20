import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # DFS topo sort
    # https://www.youtube.com/watch?v=kXy0ABd1vwo
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        NOT_VISITED=0; VISITED=1; PROCESSING=-1
        def dfs(u):
            if visited[u]==PROCESSING: return False # loop found
            if visited[u]==VISITED: return True
            visited[u]=PROCESSING
            for v in g[u]:
                if not dfs(v): return False
            visited[u]=VISITED
            return True

        visited = [NOT_VISITED for _ in range(numCourses)]
        g=defaultdict(list)
        for x,y in prerequisites: g[y].append(x)
        for u in range(numCourses):
            if not dfs(u): return False
        return True

class Solution2:
    # in degree. bfs topo sort
    # https://www.youtube.com/watch?v=kXy0ABd1vwo
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        g,incoming= defaultdict(list), [0] * n
        for u,v in prerequisites: g[v].append(u)
        for u,_ in prerequisites: incoming[u]+=1
        st=[i for i in range(n) if incoming[i]==0]
        courseTaken=0
        while st: # level by level is not necessary. stack or queue both can do the job
            u=st.pop()
            courseTaken+=1
            for v in g[u]:
                incoming[v]-=1
                if incoming[v]==0: st.append(v)
        return courseTaken==n
class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(True,get_sol().canFinish(2,[[1,0]]))
    def test2(self):
        self.assertEqual(False,get_sol().canFinish(2,[[1,0],[0,1]]))
    def test3(self):
        self.assertEqual(True,get_sol().canFinish(1, []))
    def test4(self):
        self.assertEqual(True,get_sol().canFinish(2, []))
    def test5(self):
        self.assertEqual(True,get_sol().canFinish(4, [[0,3],[1,3],[2,0],[2,1]]))
    def test6(self):
        self.assertEqual(True,get_sol().canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))
    # def test7(self):
