import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class Solution(object):
    # https://www.youtube.com/watch?v=krL3r7MY7Dc
    def pacificAtlantic(self, matrix):
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])

        def bfs(reachable_ocean):
            q = deque(reachable_ocean)
            while q:
                (i, j) = q.popleft()
                for (di, dj) in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                    new_i,new_j= di+i,dj+j
                    if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in reachable_ocean \
                            and matrix[new_i][new_j] >= matrix[i][j]: # it's '>=' not '<='
                        q.append( (new_i,new_j) )
                        reachable_ocean.add( (new_i, new_j) )
            return reachable_ocean

        pacific  =set ( [ (i, 0) for i in range(m)]   + [(0, j) for j  in range(1, n)])
        atlantic =set ( [ (i, n-1) for i in range(m)] + [(m-1, j) for j in range(n-1)])
        common =  bfs(pacific).intersection(bfs(atlantic))
        common = list(map(list,common))
        return common

class tester(unittest.TestCase):
    def test1(self):
        heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        Output= [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        expected = Solution().pacificAtlantic(heights)
        self.assertEqual(sorted(Output),sorted(expected))