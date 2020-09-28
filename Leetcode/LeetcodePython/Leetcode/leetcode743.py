import collections
import heapq


class Solution:
    def networkDelayTime(self, times, N, K) -> int:
        dist = [float("inf") for _ in range(N)]
        dist[K-1] = 0
        for _ in range(N-1):
            for u,v,w in times:
                if dist[u-1] + w < dist[v-1]: #1 based indexing
                    dist[v-1] = dist[u-1] + w

        return max(dist) if max(dist) < float("inf") else -1