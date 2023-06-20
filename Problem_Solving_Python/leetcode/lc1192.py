import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=Rhxs4k6DyMM
    # https://gist.github.com/SuryaPratapK/2774cb957a27448b485609418e272f2b
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(u):
            nonlocal time
            low[u]=disc[u]=time
            time+=1
            for v in g[u]:
                if disc[v]==-1:
                    parent[v]=u
                    dfs(v)
                    low[u]=min(low[u],low[v])
                    if low[v]>disc[u]:
                        res.append([u,v])
                else: # backedge found if not parent
                    if v==parent[u]: continue # ignore parent
                    low[u]=min(low[u],disc[v])



        disc=[-1]*n # what time it is visited first
        low=[-1]*n # lowest discovery time of back edges except the edge to the parent
        parent=[-1]*n
        res=[]
        g = defaultdict(set)
        for u,v in connections:
            g[u].add(v)
            g[v].add(u)

        time=0
        dfs(0)
        return res
class Solution2:
    # tle. time O(E*(V+E))
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = defaultdict(set)
        for u,v in connections:
            g[u].add(v)
            g[v].add(u)
        def one_component(u, vis): # dfs
            if u in vis: return True
            vis.addInReverse(u)
            for nei in g[u]:
                one_component(nei,vis)
            if len(vis)!=n: return False
            return True

        res = []
        for u,v in connections:
            g[u].remove(v)
            g[v].remove(u)
            if not one_component(0,set()):
                res.append([u,v])
            g[u].add(v)
            g[v].add(u)
        return res
class Solution3:
    # wrong ans
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def one_connection():
            for u in g:
                if len(g[u])==1:
                    v=list(g[u])[0]
                    return u,v
            return -1,-1

        res=[]
        g=defaultdict(set)
        for u,v in connections:
            g[u].add(v)
            g[v].add(u)
        while True:
            u,v = one_connection()
            if u==-1: break
            res.append([u,v])
            g[u].remove(v)
            g[v].remove(u)
        return res

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([[1,3]],get_sol().criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))
    def test02(self):
        self.assertEqual([[0,1]],get_sol().criticalConnections(2,  [[0,1]]))
    def test03(self):
        self.assertEqual([[1,3]],get_sol().criticalConnections(6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]))
