import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
# dp
class Solution:
    def updateMatrix(self, matrix):
        m, n = len(matrix), len(matrix and matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = float("inf")
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    if i > 0 and matrix[i - 1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i - 1][j] + 1
                    if j > 0 and matrix[i][j - 1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j - 1] + 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if matrix[i][j] != 0:
                    if i + 1 < m and matrix[i + 1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i + 1][j] + 1
                    if j + 1 < n and matrix[i][j + 1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j + 1] + 1
        return matrix

# bfs. multiple sources
# https://leetcode.com/problems/01-matrix/discuss/101080/Python-Simple-with-Explanation/572411
class Solution2:
    def updateMatrix(self, matrix):
        # So this problem asks us to find the minimum distance of 0  from every cell with value 1,
        # BFS should ring in your mind and instead of our single-source BFS, we
        # Apply multiple source BFS.
        m, n = len(matrix), len(matrix[0])
        q = deque()
        res = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):

                if matrix[i][j] == 0:
                    # The distance to itself is 0 and add all sources here to queue
                    res[i][j] = 0
                    q.append((i, j))
        while q:
            curI, curJ = q.popleft()
            for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                neighBorI, neighBorJ = curI + i, curJ + j
                # Validate all the neighbors and validate the distance as well
                if 0 <= neighBorI < m and 0 <= neighBorJ < n and res[neighBorI][neighBorJ] == -1:
                    res[neighBorI][neighBorJ] = res[curI][curJ] + 1
                    q.append((neighBorI, neighBorJ))

        return res

# for dfs
# https://leetcode.com/problems/01-matrix/discuss/101060/Java-DFS-solution-beat-95
# class Solution3:
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

# Wrong
class Solution4:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n=len(matrix),len(matrix[0])
        dp = [[-1]*n for _ in range(m)]
        def dfs(x,y):
            if x<0 or y<0 or x>m-1 or y>n-1: return float('inf')
            if matrix[x][y]==-1: return float('inf')
            if matrix[x][y]==0: return 0
            if dp[x][y]!=-1: return dp[x][y]
            minn=float('inf')
            matrix[x][y]=-1 # to avoid infinite loop. recursive func was called from here.
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                minn=min(minn,1+dfs(x+dx,y+dy))
            matrix[x][y]=1 # undo changes. to avoid infinite loop
            dp[x][y]=minn
            return minn

        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j]=dfs(i,j)
        return res

class tester(unittest.TestCase):
    def test1(self):
        Input= [[0,0,0], [0,1,0], [0,0,0]]
        Output= [[0,0,0], [0,1,0], [0,0,0]]
        self.assertEqual(Output,Solution().updateMatrix(Input))
    def test2(self):
        Input= [[0,0,0], [0,1,0], [1,1,1]]
        Output= [[0,0,0], [0,1,0], [1,2,1]]
        self.assertEqual(Output,Solution().updateMatrix(Input))
    def test3(self):
        Input= [[0,0,1,0,1,1,1,0,1,1],
                [1,1,1,1,0,1,1,1,1,1],
                [1,1,1,1,1,0,0,0,1,1],
                [1,0,1,0,1,1,1,0,1,1],
                [0,0,1,1,1,0,1,1,1,1],
                [1,0,1,1,1,1,1,1,1,1],
                [1,1,1,1,0,1,0,1,0,1],
                [0,1,0,0,0,1,0,0,1,1],
                [1,1,1,0,1,1,0,1,0,1],
                [1,0,1,1,1,0,1,1,1,0]]
        Output= [[0,0,1,0,1,2,1,0,1,2],
                 [1,1,2,1,0,1,1,1,2,3],
                 [2,1,2,1,1,0,0,0,1,2],
                 [1,0,1,0,1,1,1,0,1,2],
                 [0,0,1,1,1,0,1,1,2,3],
                 [1,0,1,2,1,1,1,2,1,2],
                 [1,1,1,1,0,1,0,1,0,1],
                 [0,1,0,0,0,1,0,0,1,2],
                 [1,1,1,0,1,1,0,1,0,1],
                 [1,0,1,1,1,0,1,2,1,0]]
        self.assertEqual(Output,Solution().updateMatrix(Input))
