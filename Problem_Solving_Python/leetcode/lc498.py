from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # when out of bounds move one step right and change direction. Then continue until a valid cell is found.
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        TOP_RIGHT=[-1,1]
        BOTTOM_LEFT=[1,-1]
        def valid(x,y): return 0<=x<m and 0<=y<n
        def changeDir(dx,dy):
            return BOTTOM_LEFT if [dx,dy]==TOP_RIGHT else TOP_RIGHT

        m,n=len(mat),len(mat[0])
        x,y=0,0
        res=[]
        dx,dy=TOP_RIGHT
        while len(res)!=m*n:
            if not valid(x,y): # when out of bounds move one step right and change direction
                dx,dy=changeDir(dx,dy)
                x,y=x,y+1 # move right
            while len(res)!=m*n and not valid(x,y): # then continue until a valid cell is found
                x,y=x+dx,y+dy
            res.append(mat[x][y])
            x,y=x+dx,y+dy
        return res

class Solution5:
    # https://www.youtube.com/watch?v=NTF7sDU0IWA
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

class Tester(unittest.TestCase):
    def test01(self):
        mat = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual([1,2,4,7,5,3,6,8,9],get_sol().findDiagonalOrder(mat))
    def test02(self):
        mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
        self.assertEqual([1,2,6,11,7,3,4,8,12,16,21,17,13,9,5,10,14,18,22,23,19,15,20,24,25],get_sol().findDiagonalOrder(mat))
    def test03(self):
        mat = [[1,2],[3,4]]
        self.assertEqual([1,2,3,4],get_sol().findDiagonalOrder(mat))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
    # def test11(self):
    # def test12(self):
