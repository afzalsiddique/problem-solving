import collections
import heapq
from typing import List

# dijkstra
# https://www.youtube.com/watch?v=pSqmAO-m7Lk&t=230s
# leetcode original solution
class Solution:
    def networkDelayTime(self, times, n, src):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, src)]
        dist = {}
        while pq:
            cur_dist, u = heapq.heappop(pq)
            if u in dist: continue
            dist[u] = cur_dist
            for v, new_distance in graph[u]:
                if v not in dist:
                    heapq.heappush(pq, (cur_dist+new_distance, v))

        return max(dist.values()) if len(dist) == n else -1


# dijkstra basic implementaion
class Solution2:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [float("inf") for _ in range(N)]
        dist[K-1] = 0
        for _ in range(N-1):
            for u,v,w in times:
                if dist[u-1] + w < dist[v-1]: #1 based indexing
                    dist[v-1] = dist[u-1] + w

        return max(dist) if max(dist) < float("inf") else -1