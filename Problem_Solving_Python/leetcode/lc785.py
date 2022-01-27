from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *
def get_sol(): return Solution()
# https://leetcode.com/problems/is-graph-bipartite/discuss/115543/Easy-Python-Solution
# https://www.youtube.com/watch?v=-SpTh4AEZrk
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # colors are 0 and 1
        NOCOLOR=-1
        def dfs(u,color):
            if colors[u]!=NOCOLOR:
                return colors[u]==color
            colors[u]=color
            for v in graph[u]:
                if not dfs(v,1-color):
                    return False
            return True

        n=len(graph)
        colors=[NOCOLOR]*n
        for i in range(n):
            if colors[i]==NOCOLOR and not dfs(i,0):
                return False
        return True
class Solution2:
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



class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(False, Solution().isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
    def test02(self):
        self.assertEqual(True, Solution().isBipartite([[1,3],[0,2],[1,3],[0,2]]))
