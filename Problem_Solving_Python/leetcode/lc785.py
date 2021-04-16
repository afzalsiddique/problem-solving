# https://leetcode.com/problems/is-graph-bipartite/discuss/115543/Easy-Python-Solution
# https://www.youtube.com/watch?v=-SpTh4AEZrk
import unittest
from random import random, randrange
from typing import List

from collections import deque



class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # colors are 0 and 1
        n = len(graph)
        color = {}
        def dfs(node):
            for neigh in graph[node]:
                if neigh in color:
                    if color[node]==color[neigh]:return False
                else:
                    color[neigh] = 1-color[node]
                    if not dfs(neigh):return False
            return True

        for i in range(n):
            if i not in color:
                color[i] = 1
                if not dfs(i):return False
        return True


class tester(unittest.TestCase):

    def test_1(self):
        self.assertEqual(False, Solution().isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
    def test2(self):
        self.assertEqual(True, Solution().isBipartite([[1,3],[0,2],[1,3],[0,2]]))
