from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import cache; from heapq import *; import unittest; from typing import List, Optional; import functools;from sortedcontainers import SortedList,SortedDict
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # abdul bari video
    # https://www.youtube.com/watch?v=XB4MIexjvY0
    def networkDelayTime(self, times, n, src):
        def dijkstra(g):
            final_dist = [float('inf') for _ in range(n)]
            final_dist[src]=0
            pq=[(0,src)]

            # according to abdul bari video but not necessary
            # for v,w in g[src]: final_dist[v]=w
            # for v,w in g[src]: pq.append((w,v))
            # heapify(pq)

            while pq:
                cur,u=heappop(pq)
                if cur>final_dist[u]: continue # optimization
                for v,cost in g[u]:
                    if cur+cost<final_dist[v]:
                        final_dist[v]=cur+cost
                        heappush(pq,(cur+cost,v))
            return final_dist

        src-=1 # convert to 0 based indexing
        g=defaultdict(list)
        for u,v,w in times: g[u-1].append((v-1,w)) # convert to 0 based indexing

        final_dist = dijkstra(g)
        res = max(final_dist)
        return res if res!=float('inf') else -1
class Solution2:
    # dijkstra heap implementaion
    # https://www.youtube.com/watch?v=pSqmAO-m7Lk&t=230s
    # leetcode original solution
    def networkDelayTime(self, times, n, src):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, src)]
        cost = {}
        while pq:
            cur_dist, u = heappop(pq)
            if u in cost: continue
            cost[u] = cur_dist
            for v, new_distance in graph[u]:
                if v not in cost:
                    heappush(pq, (cur_dist+new_distance, v))

        return max(cost.values()) if len(cost) == n else -1
# adjacency matrix version
class Solution3:
    def networkDelayTime(self, times, n, src):
        graph = [[None]*(n+1) for _ in range(n+1)]
        for u, v, w in times:
            graph[u][v]=w

        pq = [(0, src)]
        dist = {}
        while pq:
            cur_dist, u = heappop(pq)
            if u in dist: continue
            dist[u] = cur_dist
            for v in range(n+1):
                if graph[u][v]!=None and v not in dist:
                    heappush(pq, (cur_dist+graph[u][v],v))
        return max(dist.values()) if len(dist) == n else -1


# dijkstra basic implementaion
class Solution4:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [float("inf") for _ in range(N)]
        dist[K-1] = 0
        for _ in range(N-1):
            for u,v,w in times:
                if dist[u-1] + w < dist[v-1]: #1 based indexing
                    dist[v-1] = dist[u-1] + w

        return max(dist) if max(dist) < float("inf") else -1


class MyTestCase(unittest.TestCase):
    def test1(self):
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]; N = 4; K = 2
        expected = 2
        self.assertEqual(expected, get_sol().networkDelayTime(times, N, K))
    def test2(self):
        times = [[1,2,1]]; N = 2; K = 2
        expected = -1
        self.assertEqual(expected, get_sol().networkDelayTime(times, N, K))
    def test3(self):
        times = [[1,2,1]]; N = 2; K = 1
        expected = 1
        self.assertEqual(expected, get_sol().networkDelayTime(times, N, K))
    def test4(self):
        times =[[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]]; N = 5; K = 5
        expected = 31
        self.assertEqual(expected, get_sol().networkDelayTime(times, N, K))
