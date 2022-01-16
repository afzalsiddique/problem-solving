import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
# ############similar to 1631####
class Solution:
    #### Prim's Algo ####
    def minCostConnectPoints(self, p: List[List[int]]) -> int:

        def manhattan(x, y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])

        ans, n = 0, len(p)
        seen = set()
        vertices = [(0, 'dummy', 0)] # (dist, dummy, nextnode)

        while len(seen) < n:
            # print(vertices, seen)
            dist, u, v= heappop(vertices)
            if v in seen: continue
            ans += dist
            seen.add(v)
            for neigh in range(n):
                if neigh not in seen and neigh!=v:
                    man_dist = manhattan(p[neigh], p[v])
                    heappush(vertices, (man_dist, v, neigh))
        return ans

class Solution2:
    #### Union find #######
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
        self.assertEqual(20, get_sol().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
    def test_2(self):
        self.assertEqual(18, get_sol().minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
    def test_3(self):
        self.assertEqual(4, get_sol().minCostConnectPoints([[0,0],[1,1],[1,0],[-1,1]]))
    def test_4(self):
        self.assertEqual(4000000, get_sol().minCostConnectPoints([[-1000000,-1000000],[1000000,1000000]]))
    def test_5(self):
        self.assertEqual(0, get_sol().minCostConnectPoints([[0,0]]))
