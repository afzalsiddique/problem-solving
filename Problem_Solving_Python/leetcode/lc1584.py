from heapq import *
import unittest
from collections import defaultdict
from typing import List

# ############similar to 1631####
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        roots = {}

        def add(x):
            if x not in roots:
                roots[x] = x

        def find(x):
            if x in roots:
                p = roots[x]
            else:
                p = x
            if p==x:
                return x
            roots[x] = find(roots[x])
            return roots[x]

        def union(x,y):
            add(x), add(y)
            roots[find(x)] = roots[find(y)]


        def dist(point1, point2): # manhattan distance
            x1, y1 = point1
            x2, y2 = point2
            return abs(x2-x1) + abs(y2-y1)

        edge_to_nodes = defaultdict(list) # key->edge weight, value-> list(pair of nodes connected with that edge). value is a list because there can be same edge value for different pair of nodes
        edges = []
        for i in range(n):
            for j in range(i+1, n): # upper half of the matrix
                if i==j:
                    continue
                distance = dist(points[i],points[j])
                edge_to_nodes[distance].append((i,j))
                edges.append(distance)

        heapify(edges)
        cnt = 0
        summ = 0
        while(True):
            if cnt == n-1: # maximum node-1 edges in minimum spanning tree
                break
            edge = heappop(edges)
            node1, node2 = edge_to_nodes[edge].pop()
            if find(node1) != find(node2):
                union(node1, node2)
                summ += edge
                cnt += 1
        return summ


class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = 20
        actual = sol.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = 18
        actual = sol.minCostConnectPoints([[3,12],[-2,5],[-4,1]])
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = 4
        actual = sol.minCostConnectPoints([[0,0],[1,1],[1,0],[-1,1]])
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = 4000000
        actual = sol.minCostConnectPoints([[-1000000,-1000000],[1000000,1000000]])
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = 0
        actual = sol.minCostConnectPoints([[0,0]])
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        expected = 0
        actual = sol.minCostConnectPoints(0)
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        expected = 0
        actual = sol.minCostConnectPoints(0)
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        expected = 0
        actual = sol.minCostConnectPoints(0)
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        expected = 0
        actual = sol.minCostConnectPoints(0)
        self.assertEqual(expected, actual)