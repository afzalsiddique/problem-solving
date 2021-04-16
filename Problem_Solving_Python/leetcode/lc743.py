from collections import defaultdict
from heapq import *
import unittest
from typing import List

# dijkstra
# https://www.youtube.com/watch?v=pSqmAO-m7Lk&t=230s
# leetcode original solution
class Solution:
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
class Solution2:
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
class Solution3:
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
        solution = Solution()
        actual = solution.networkDelayTime(times, N, K)
        expected = 2
        self.assertEqual(expected, actual)
    def test2(self):
        times = [[1,2,1]]
        N = 2
        K = 2
        solution = Solution()
        actual = solution.networkDelayTime(times, N, K)
        expected = -1
        self.assertEqual(expected, actual)
    def test3(self):
        times = [[1,2,1]]
        N = 2
        K = 1
        solution = Solution()
        actual = solution.networkDelayTime(times, N, K)
        expected = 1
        self.assertEqual(expected, actual)
    def test4(self):
        times =[[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]]
        N = 5
        K = 5
        solution = Solution()
        actual = solution.networkDelayTime(times, N, K)
        expected = 31
        self.assertEqual(expected, actual)
