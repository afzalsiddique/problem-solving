import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

# https://www.youtube.com/watch?v=NTF7sDU0IWA
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix),len(matrix[0])
        res=[]
        row,col=0,0
        going_up = 1
        while row<m and col<n:
            if going_up:
                while row>0 and col<n-1:
                    res.append(matrix[row][col])
                    row-=1
                    col+=1
                res.append(matrix[row][col])
                if col==n-1:
                    row+=1
                else:
                    col+=1
            else:
                while col>0 and row<m-1:
                    res.append(matrix[row][col])
                    row+=1
                    col-=1
                res.append(matrix[row][col])
                if row==m-1:
                    col+=1
                else:
                    row+=1
            going_up=1-going_up
        return res

# leetcode original. squeezed version of the previous solution
class Solution2:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        N, M = len(matrix), len(matrix[0])
        row, column = 0, 0
        going_up = 1
        result = []
        while row < N and column < M:
            result.append((matrix[row][column]))
            # result.append((row,column))
            new_row = row + (-1 if going_up == 1 else 1)
            new_column = column + (1 if going_up == 1 else -1)
            if new_row < 0 or new_row == N or new_column < 0 or new_column == M:
                if going_up:
                    row += (column == M - 1)
                    column += (column < M - 1)
                else:
                    column += (row == N - 1)
                    row += (row < N - 1)
                going_up = 1 - going_up
            else:
                row = new_row
                column = new_column
        return result

# leetcode original
class Solution3:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        N, M = len(matrix), len(matrix[0])
        result, intermediate = [], []
        for d in range(N + M - 1):
            intermediate.clear()
            r, c = 0 if d < M else d - M + 1, d if d < M else M - 1
            while r < N and c > -1:
                intermediate.append(matrix[r][c])
                r += 1
                c -= 1
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        return result

# https://leetcode.com/problems/diagonal-traverse/discuss/581868/Easy-Python-NO-DIRECTION-CHECKING
class Solution4:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def comp(x):
            if (x[0]+x[1])%2:
                return (x[0])
            return (-x[0])


        di = defaultdict(list)
        res = []
        m,n=len(mat),len(mat[0])
        for i in range(m):
            for j in range(n):
                di[i+j].append((i,j))
        for key in di:
            di[key].sort(key=comp)
        for ii in range(m+n+1):
            for i,j in di[ii]:
                res.append(mat[i][j])
        return res
class tester(unittest.TestCase):
    def test1(self):
        mat = [[1,2,3],[4,5,6],[7,8,9]]
        Output= [1,2,4,7,5,3,6,8,9]
        self.assertEqual(Output,Solution().findDiagonalOrder(mat))
    def test2(self):
        mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
        Output= [1,2,4,7,5,3,6,8,9]
        self.assertEqual(Output,Solution().findDiagonalOrder(mat))
