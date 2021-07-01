import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        EMPTY= -1
        colors = [EMPTY]*(n+1)
        g=defaultdict(list)
        vis=set()
        for x,y in paths:
            g[x].append(y)
            g[y].append(x)

        def feasible(color,u):
            for neigh in g[u]:
                if colors[neigh]==color:
                    return False
            return True

        def put_color(u): # dfs+backtrack
            if u in vis: return True
            for color in range(1,4+1):
                if feasible(color,u):
                    colors[u]=color
                    vis.add(u)
                    for neigh in g[u]:
                        if put_color(neigh): return True
                    vis.remove(u)
                    colors[u]=color
            return False

        for i in range(1,n+1):
            put_color(i)
        return colors[1:]





class tester(unittest.TestCase):
    def test01(self):
        n = 3
        paths = [[1,2],[2,3],[3,1]]
        Output= [1,2,3]
        self.assertEqual(Output,get_sol().gardenNoAdj(n,paths))
    def test02(self):
        n = 4
        paths = [[1,2],[3,4]]
        Output= [1,2,1,2]
        self.assertEqual(Output,get_sol().gardenNoAdj(n,paths))
    def test03(self):
        n = 4
        paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
        Output= [1,2,3,4]
        self.assertEqual(Output,get_sol().gardenNoAdj(n,paths))
    # def test04(self):
    # def test05(self):