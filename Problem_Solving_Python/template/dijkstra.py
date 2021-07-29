import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
# https://leetcode.com/problems/network-delay-time/
class Solution:
    # abdul bari video. edge relaxation and heap based implementation
    # https://www.youtube.com/watch?v=XB4MIexjvY0
    def networkDelayTime(self, times, n, src):
        g=defaultdict(list)
        for u,v,w in times: g[u].append((v,w))

        final_dist = [float('inf') for _ in range(n+1)] # 1 based indexing
        final_dist[0]=float('-inf') # invalid index i.e index starts from 1
        final_dist[src]=0
        for v,w in g[src]: final_dist[v]=w

        pq=[(0,src)]
        for v,w in g[src]: pq.append((w,v))
        heapify(pq)
        while pq:
            src_to_u,u=heappop(pq)
            for v,dist_between_uv in g[u]:
                new_dist=src_to_u+dist_between_uv
                if new_dist<final_dist[v]:
                    final_dist[v]=new_dist
                    heappush(pq,(new_dist,v))
        res = max(final_dist)
        return res if res!=float('inf') else -1
class Solution2:
    # dijkstra heap implementation
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
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        N = 4
        K = 2
        actual = get_sol().networkDelayTime(times, N, K)
        expected = 2
        self.assertEqual(expected, actual)
    def test2(self):
        times = [[1,2,1]]
        N = 2
        K = 2
        actual = get_sol().networkDelayTime(times, N, K)
        expected = -1
        self.assertEqual(expected, actual)
    def test3(self):
        times = [[1,2,1]]
        N = 2
        K = 1
        actual = get_sol().networkDelayTime(times, N, K)
        expected = 1
        self.assertEqual(expected, actual)
    def test4(self):
        times =[[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]]
        N = 5
        K = 5
        actual = get_sol().networkDelayTime(times, N, K)
        expected = 31
        self.assertEqual(expected, actual)
