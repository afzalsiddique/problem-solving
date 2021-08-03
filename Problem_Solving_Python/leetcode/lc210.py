import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=ddTC4Zovtbc
    # topological sort
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        NOT_VISITED=0; VISITED=1; PROCESSING=-1
        visited = [NOT_VISITED for _ in range(numCourses)]
        st=[]
        g=defaultdict(list)
        for x,y in prerequisites: g[x].append(y)
        def dfs(u):
            if visited[u]==PROCESSING: return False
            if visited[u]==VISITED: return True
            visited[u]=PROCESSING
            for v in g[u]:
                if not dfs(v): return False
            visited[u]=VISITED
            st.append(u)
            return True

        for u in range(numCourses):
            if not dfs(u): return []
        return st

class Tester(unittest.TestCase):
    def test_1(self):
        a = Solution().findOrder(2,[[1,0]])
        self.assertEqual([0,1],a)
    def test_2(self):
        a = Solution().findOrder(4,[[1,0],[2,0],[3,1],[3,2]])
        self.assertEqual([0,1,2,3],a)
    def test_3(self):
        a = Solution().findOrder(1,[])
        self.assertEqual([0],a)
    def test_4(self):
        a = Solution().findOrder(2,[[0,1],[1,0]])
        self.assertEqual([],a)
