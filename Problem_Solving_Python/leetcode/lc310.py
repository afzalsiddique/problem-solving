import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List



class Solution:
    # https://www.youtube.com/watch?v=ZfzVig8UqBQ
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [x for x in range(n)]

        graph = [set() for _ in range(n)]
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start)

        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)

        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            temp = []

            for leaf in leaves:
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)
                    if len(graph[neighbor]) == 1:
                        temp.append(neighbor)
            leaves = temp

        return leaves

class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([3,4],Solution().findMinHeightTrees(n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]))