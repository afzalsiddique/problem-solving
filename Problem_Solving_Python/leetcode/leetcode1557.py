from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        in_degree = [0] * n
        for u, v in edges:
            in_degree[v] += 1
        vertices = []
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                vertices.append(i)
        return vertices





        # return list(set(range(n)) - set(e[1] for e in edges))