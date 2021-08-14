import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # bfs
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        g=defaultdict(set)
        for x,y in adjacentPairs:
            g[x].add(y)
            g[y].add(x)
        head=None
        for x in g:
            if len(g[x])==1:
                head=x
                break
        vis=set()
        q=deque([head])
        res=[]
        while q:
            for _ in range(len(q)):
                u=q.pop()
                if u in vis: continue
                vis.add(u)
                res.append(u)
                for v in g[u]:
                    q.append(v)
        return res

class MyTestCase(unittest.TestCase):
    def test_1(self):
        adjacentPairs = [[2,1],[3,4],[3,2]]
        Output= [1,2,3,4]
        self.assertEqual(Output, get_sol().restoreArray(adjacentPairs))
    def test_2(self):
        adjacentPairs = [[4,-2],[1,4],[-3,1]]
        Output= [-2,4,1,-3]
        self.assertEqual(Output, get_sol().restoreArray(adjacentPairs))
    def test_3(self):
        adjacentPairs = [[100000,-100000]]
        Output= [100000,-100000]
        self.assertEqual(Output, get_sol().restoreArray(adjacentPairs))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):