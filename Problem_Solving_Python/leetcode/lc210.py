import unittest
from collections import deque
from heapq import *
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g=[[] for _ in range(numCourses)]
        visited=['notvisited' for _ in range(numCourses)]
        for x,y in prerequisites:
            g[y].append(x)
        st = []
        def dfs(i):
            if visited[i]=='processing':
                return False
            if visited[i]=='visited':
                return True
            visited[i]='processing'
            for v in g[i]:
                if not dfs(v):
                    return False
            st.append(i)
            visited[i]='visited'
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return st[::-1]

class case(unittest.TestCase):
    def test_1(self):
        a = Solution().findOrder(2,[[1,0]])
        self.assertEqual([0,1],a)
    def test_2(self):
        a = Solution().findOrder(4,[[1,0],[2,0],[3,1],[3,2]])
        self.assertEqual([0,2,1,3],a)
    def test_3(self):
        a = Solution().findOrder(1,[])
        self.assertEqual([0],a)
    def test_4(self):
        a = Solution().findOrder(2,[[0,1],[1,0]])
        self.assertEqual([],a)
