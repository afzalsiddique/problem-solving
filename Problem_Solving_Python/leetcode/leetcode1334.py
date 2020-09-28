import collections
import math
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = [[math.inf]*n for i in range(n)]
        for i in range(n):
            g[i][i] = 0
        for u,v,w in edges:
            g[u][v] = w
            g[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    g[i][j] = min(g[i][j], g[i][k]+g[k][j])
        res_node = -1
        res_connected = math.inf
        for i in range(n):
            conn = 0
            for j in range(n):
                if g[i][j] <= distanceThreshold:
                    conn+=1
            if conn <= res_connected:
                res_connected = conn
                res_node = i
        return res_node