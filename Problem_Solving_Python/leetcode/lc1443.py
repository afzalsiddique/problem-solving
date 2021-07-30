import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.cost = 0
        def dfs(root):
            if not graph[root]: return hasApple[root]
            cur_apple = hasApple[root] # if this node or its neighbors have apples
            for child in graph[root]:
                if child not in visited:
                    visited.add(child)
                    if dfs(child):
                        self.cost += 2
                        cur_apple |= True
            return cur_apple or hasApple[root]

        graph = defaultdict(list)
        for f,t in edges:
            graph[f].append(t)
            graph[t].append(f)

        visited = {0}
        dfs(0)
        return self.cost

class MyTestCase(unittest.TestCase):
    def test_1(self):
        n,edges,hasApple = 7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,False,True,False,True,True,False]
        Output= 8
        self.assertEqual(Output,get_sol().minTime(n,edges,hasApple))
    def test_2(self):
        n,edges,hasApple = 7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,False,True,False,False,True,False]
        Output= 6
        self.assertEqual(Output,get_sol().minTime(n,edges,hasApple))
    def test_3(self):
        n,edges,hasApple = 7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,False,False,False,False,False,False]
        Output= 0
        self.assertEqual(Output,get_sol().minTime(n,edges,hasApple))
    def test_4(self):
        n,edges,hasApple = 4, [[0,2],[0,3],[1,2]], [False,True,False,False]
        Output= 4
        self.assertEqual(Output,get_sol().minTime(n,edges,hasApple))
