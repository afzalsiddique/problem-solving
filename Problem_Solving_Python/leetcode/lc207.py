import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # DFS
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
    # in degree
    # https://www.youtube.com/watch?v=kXy0ABd1vwo
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for x,y in prerequisites:
            graph[x].append(y)
            indegree[y]+=1

        cnt = 0
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while q:
            curr = q.popleft()
            if indegree[curr]==0:
                cnt+=1
            for u in graph[curr]:
                indegree[u]-=1
                if indegree[u]==0:
                    q.append(u)
        if cnt==numCourses:
            return True
        return False
class Tester(unittest.TestCase):
    def test1(self):
        numCourses,prerequisites = 2,[[1,0]]
        Output= True
        self.assertEqual(Output,get_sol().canFinish(numCourses,prerequisites))
    def test2(self):
        numCourses,prerequisites = 2,[[1,0],[0,1]]
        Output= False
        self.assertEqual(Output,get_sol().canFinish(numCourses,prerequisites))
    def test3(self):
        numCourses,prerequisites = 1, []
        Output= True
        self.assertEqual(Output,get_sol().canFinish(numCourses,prerequisites))
    def test4(self):
        numCourses,prerequisites = 2, []
        Output= True
        self.assertEqual(Output,get_sol().canFinish(numCourses,prerequisites))
    def test5(self):
        numCourses,prerequisites = 5, [[1,4],[2,4],[3,1],[3,2]]
        Output= True
        self.assertEqual(Output,get_sol().canFinish(numCourses,prerequisites))
    # def test6(self):
    # def test7(self):
