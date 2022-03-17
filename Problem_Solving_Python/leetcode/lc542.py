from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution5:
    # bfs
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        res=[[float('inf')]*n for _ in range(m)]
        q=deque([[x,y] for x in range(m) for y in range(n) if mat[x][y]==0])
        cnt=0
        while q:
            for _ in range(len(q)):
                x,y=q.popleft()
                if res[x][y]!=float('inf'): continue
                res[x][y]=cnt
                for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                    X,Y=x+dx,y+dy
                    if not 0<=X<m or not 0<=Y<n: continue
                    if res[X][Y]==float('inf'):
                        q.append([X,Y])
            cnt+=1
        return res
class Solution:
    # dp
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
            x, y = q.popleft()
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                neighBorI, neighBorJ = x + dx, y + dy
                # Validate all the neighbors and validate the distance as well
                if 0 <= neighBorI < m and 0 <= neighBorJ < n and res[neighBorI][neighBorJ] == -1:
                    res[neighBorI][neighBorJ] = res[x][y] + 1
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
    def test01(self):
        Input= [[0,0,0], [0,1,0], [0,0,0]]
        Output= [[0,0,0], [0,1,0], [0,0,0]]
        self.assertEqual(Output,get_sol().updateMatrix(Input))
    def test02(self):
        Input= [[0,0,0], [0,1,0], [1,1,1]]
        Output= [[0,0,0], [0,1,0], [1,2,1]]
        self.assertEqual(Output,get_sol().updateMatrix(Input))
    def test03(self):
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
        self.assertEqual(Output,get_sol().updateMatrix(Input))
    def test04(self):
        self.assertEqual([[2,1,0,0,1,0,0,1,1,0],[1,0,0,1,0,1,1,2,2,1],[1,1,1,0,0,1,2,2,1,0],[0,1,2,1,0,1,2,3,2,1],[0,0,1,2,1,2,1,2,1,0],[1,1,2,3,2,1,0,1,1,1],[0,1,2,3,2,1,1,0,0,1],[1,2,1,2,1,0,0,1,1,2],[0,1,0,1,1,0,1,2,2,3],[1,2,1,0,1,0,1,2,3,4]],get_sol().updateMatrix([[1,1,0,0,1,0,0,1,1,0],[1,0,0,1,0,1,1,1,1,1],[1,1,1,0,0,1,1,1,1,0],[0,1,1,1,0,1,1,1,1,1],[0,0,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,0,1,1,1],[0,1,1,1,1,1,1,0,0,1],[1,1,1,1,1,0,0,1,1,1],[0,1,0,1,1,0,1,1,1,1],[1,1,1,0,1,0,1,1,1,1]]))
    def test05(self):
        self.assertEqual([[0, 0, 1, 0, 1, 2], [1, 1, 2, 1, 0, 1]],get_sol().updateMatrix([[0,0,1,0,1,1], [1,1,1,1,0,1], ]))
