import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        g=defaultdict(list)
        for u,v,w in edges:
            g[u].append((v,w))
            g[v].append((u,w))

        def dijkstra():
            final_dist = [float('inf') for _ in range(n+1)] # 1 based
            final_dist[n]=0

            pq=[(0,n)]

            while pq:
                cur,u = heappop(pq)
                for v,cost in g[u]:
                    if cur+cost<final_dist[v]:
                        final_dist[v]=cur+cost
                        heappush(pq,(cur+cost,v))

            return final_dist

        dp = {}
        def dfs(u):
            if u in dp: return dp[u]
            if u==n: return 1
            ans=0
            for v,_ in g[u]:
                if final_dist[u]>final_dist[v]:
                    ans += dfs(v)
                    ans%=10**9+7
            dp[u]=ans
            return ans

        final_dist = dijkstra()
        ans = dfs(1)
        return ans


class MyTestCase(unittest.TestCase):
    def test1(self):
        n,edges = 5, [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
        Output= 3
        self.assertEqual(Output, get_sol().countRestrictedPaths(n,edges))
    def test2(self):
        n,edges = 7, [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
        Output= 1
        self.assertEqual(Output, get_sol().countRestrictedPaths(n,edges))
    def test3(self):
        n,edges = 10, [[9,10,8],[9,6,5],[1,5,9],[6,8,10],[1,8,1],[8,10,7],[10,7,9],[5,7,3],[4,2,9],[2,3,9],[3,10,4],[1,4,7],[7,6,1],[3,9,8],[9,1,6],[4,7,10],[9,4,9]]
        Output= 1
        self.assertEqual(Output, get_sol().countRestrictedPaths(n,edges))
    # def test4(self):
