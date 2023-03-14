from collections import defaultdict;
from heapq import *; import unittest; from typing import List;


def get_sol(): return Solution()
# ############similar to 1584####
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r, c = len(heights), len(heights[0])
        if r == c == 1:
            return 0

        roots = {}

        def add(x):
            if x not in roots:
                roots[x] = x

        def find(x):
            if x in roots:
                p = roots[x]
            else:
                p = x
            if p == x:
                return x
            roots[x] = find(roots[x])
            return roots[x]

        def union(x, y):
            add(x), add(y)
            roots[find(x)] = roots[find(y)]

        edge_to_nodes = defaultdict(list)  # key->edge weight, value-> list(pair of nodes connected with that edge).
        # value is a list because there can be same edge value for different pair of nodes
        edges = []

        for i in range(r):
            for j in range(c):
                if i + 1 < r:
                    edge = abs(heights[i + 1][j] - heights[i][j])
                    edges.append(edge)
                    edge_to_nodes[edge].append(((i, j), (i + 1, j)))
                if i - 1 >= 0:
                    edge = abs(heights[i - 1][j] - heights[i][j])
                    edges.append(edge)
                    edge_to_nodes[edge].append(((i, j), (i - 1, j)))
                if j + 1 < c:
                    edge = abs(heights[i][j + 1] - heights[i][j])
                    edges.append(edge)
                    edge_to_nodes[edge].append(((i, j), (i, j + 1)))
                if j - 1 >= 0:
                    edge = abs(heights[i][j - 1] - heights[i][j])
                    edges.append(edge)
                    edge_to_nodes[edge].append(((i, j), (i, j - 1)))

        heapify(edges)
        maxx = float('-inf')
        start, end = (0, 0), (r - 1, c - 1)
        while find(start) != find(end):
            edge = heappop(edges)
            node1, node2 = edge_to_nodes[edge].pop()
            if find(node1) != find(node2):
                union(node1, node2)
                maxx = max(maxx, edge)

        return maxx


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(2, get_sol().minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
    def test02(self):
        self.assertEqual(1, get_sol().minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
    def test03(self):
        self.assertEqual(0, get_sol().minimumEffortPath( [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]))
    def test04(self):
        self.assertEqual(0, get_sol().minimumEffortPath([[3]]))