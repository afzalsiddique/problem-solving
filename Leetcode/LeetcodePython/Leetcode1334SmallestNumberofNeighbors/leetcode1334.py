import collections

class Solution:
    def findTheCity(self, n, edges, distanceThreshold) -> int:
        graph = collections.defaultdict(dict)
        for i in range(n):
            for j in range(n):
                graph[i][j] = 999999