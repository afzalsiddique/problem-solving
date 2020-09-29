from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * n
        for u, v in edges:
            in_degree[v] += 1
        vertices = []
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                vertices.append(i)
        return vertices