import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    # dijkstra
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g=defaultdict(list)
        for i in range(len(edges)):
            u,v=edges[i]
            w=succProb[i]
            g[u].append((v,w))
            g[v].append((u,w))

        final_prob=[0.0 for _ in range(n)]
        final_prob[start]=1
        for v,w in g[start]: final_prob[v]=w

        pq = [(1,start)] # prob,src
        for v,w in g[start]: pq.append((-w,v))
        heapify(pq)
        while pq:
            cur_prob,u = heappop(pq)
            cur_prob*=(-1) # max_heap
            for v,bt_u_v in g[u]:
                new_prob = cur_prob*bt_u_v
                if new_prob>final_prob[v]:
                    final_prob[v]=new_prob
                    heappush(pq,(-new_prob,v))
        return final_prob[end]

class MyTestCase(unittest.TestCase):
    def test1(self):
        n,edges,succProb,start,end= 3,[[0,1],[1,2],[0,2]],[0.5,0.5,0.2],0, 2
        Output= 0.25000
        self.assertEqual(Output,get_sol().maxProbability(n,edges,succProb,start,end))
    def test2(self):
        n,edges,succProb,start,end= 3,[[0,1],[1,2],[0,2]],[0.5,0.5,0.3],0, 2
        Output= 0.30000
        self.assertEqual(Output,get_sol().maxProbability(n,edges,succProb,start,end))
    def test3(self):
        n,edges,succProb,start,end= 3,[[0,1]],[0.5],0, 2
        Output= 0.00000
        self.assertEqual(Output,get_sol().maxProbability(n,edges,succProb,start,end))
    def test4(self):
        n,edges,succProb,start,end= 5, [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]], [0.37,0.17,0.93,0.23,0.39,0.04], 3, 4
        Output= 0.21390
        self.assertEqual(Output,get_sol().maxProbability(n,edges,succProb,start,end))