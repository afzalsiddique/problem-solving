from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    # dfs. Works because 10<=time<=100
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        def dfs(u,time,score:int,vis:set[int]):
            nonlocal res
            if u==0:
                res=max(res,score)
            for v,t in g[u]:
                newVis=vis.union([v])
                newScore=score
                newTime=time+t
                if len(newVis)>len(vis): # visited a node which was never visited before
                    newScore+=values[v]
                if newTime<=maxTime:
                    dfs(v,newTime,newScore,newVis)


        g=defaultdict(list)
        for i,j,w in edges:
            g[i].append((j,w))
            g[j].append((i,w))

        res=0
        dfs(0,0,values[0],{0})
        return res
class Solution2:
    # bfs
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        def calculateQuality(cur,vis:set[int]):
            return sum(values[x] for x in vis) if cur==0 else 0
        g=defaultdict(list)
        for i,j,time in edges:
            g[i].append((j,time))
            g[j].append((i,time))

        res=0
        q=deque()
        q.append((0,{0},0)) # start,vis,time
        while q:
            u,vis,t=q.popleft()
            res=max(res,calculateQuality(u,vis))
            for v,w in g[u]:
                newTime=t+w
                if newTime<=maxTime:
                    newVis=vis.union([v])
                    q.append((v,newVis,newTime))
        return res


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(75, get_sol().maximalPathQuality([0,32,10,43],  [[0,1,10],[1,2,15],[0,3,10]],  49))
    def test2(self):
        self.assertEqual(25, get_sol().maximalPathQuality( [5,10,15,20],  [[0,1,10],[1,2,10],[0,3,10]], 30))
    def test3(self):
        self.assertEqual(7, get_sol().maximalPathQuality([1,2,3,4],  [[0,1,10],[1,2,11],[2,3,12],[1,3,13]],  50))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):
