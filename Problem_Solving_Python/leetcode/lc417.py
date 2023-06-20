from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # dfs. Go from cell with lower height to cell to higher or equal height
    def pacificAtlantic(self, mat: List[List[int]]) -> List[List[int]]:
        def valid(x,y): return 0<=x<m and 0<=y<n
        def traverse(x,y,vis):
            if (x,y) in vis: return
            vis.add((x, y))
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                if valid(x+dx,y+dy) and mat[x+dx][y+dy]>=mat[x][y]:
                    traverse(x+dx,y+dy,vis)

        m,n=len(mat),len(mat[0])
        pacificInit=set((0,j) for j in range(n)) | set((i,0) for i in range(m))
        atlanticInit=set((m-1,j) for j in range(n)) | set((i,n-1) for i in range(m))
        pacific,atlantic=set(),set()
        for x,y in pacificInit:
            traverse(x,y,pacific)
        for x,y in atlanticInit:
            traverse(x,y,atlantic)
        return list(map(list,pacific.intersection(atlantic)))
class Solution2:
    # bfs
    # https://www.youtube.com/watch?v=krL3r7MY7Dc
    def pacificAtlantic(self, mat):
        def bfs(reachable_ocean):
            q = deque(reachable_ocean)
            while q:
                (i, j) = q.popleft()
                for (di, dj) in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                    new_i,new_j= di+i,dj+j
                    if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in reachable_ocean \
                            and mat[new_i][new_j] >= mat[i][j]: # it's '>=' not '<='
                        q.append( (new_i,new_j) )
                        reachable_ocean.add((new_i, new_j))
            return reachable_ocean

        if not mat: return []
        m, n = len(mat), len(mat[0])
        pacific  =set ( [ (i, 0) for i in range(m)]   + [(0, j) for j  in range(1, n)])
        atlantic =set ( [ (i, n-1) for i in range(m)] + [(m-1, j) for j in range(n-1)])
        common =  bfs(pacific).intersection(bfs(atlantic))
        common = list(map(list,common))
        return common

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(sorted([[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]),sorted(get_sol().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])))
    def test02(self):
        self.assertEqual(sorted([[0,0],[0,1],[1,0],[1,1]]),sorted(get_sol().pacificAtlantic([[2,1],[1,2]])))