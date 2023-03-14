from collections import defaultdict;
from heapq import *; import unittest;


def get_sol(): return Solution()
class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        def dijkstra(g,src):
            final_dist = [float('inf') for _ in range(n)]
            final_dist[src]=0
            pq=[(0,src)]
            while pq:
                cur,u=heappop(pq)
                if cur>final_dist[u]: continue # optimization
                for v,cost in g[u]:
                    if cur+cost<final_dist[v]:
                        final_dist[v]=cur+cost
                        heappush(pq,(cur+cost,v))
            return final_dist

        g=defaultdict(list)
        for u,v,w in edges:
            g[u].append((v,w+1)) # 'w+1' because w nodes between them and the destination node(+1)
            g[v].append((u,w+1))

        dist=dijkstra(g,0)
        res=0
        for i in range(n):
            if dist[i]<=maxMoves:
                res+=1

        for u,v,w in edges:
            a,b=0,0
            a+=max(maxMoves-dist[u],0)
            b+=max(maxMoves-dist[v],0)
            res+=min(a+b,w)
        return res


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(13,get_sol().reachableNodes([[0,1,10],[0,2,1],[1,2,2]], 6, 3))
    def test02(self):
        self.assertEqual(23,get_sol().reachableNodes([[0,1,4],[1,2,6],[0,2,8],[1,3,1]], 10,4))
    def test03(self):
        self.assertEqual(1,get_sol().reachableNodes([[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], 17, 5))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
