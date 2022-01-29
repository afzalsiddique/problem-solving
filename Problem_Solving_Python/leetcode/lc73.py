from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

# space constant
# https://www.youtube.com/watch?v=M65xBewcqcI&t=340s
class Solution:
    def setZeroes(self,matrix: List[List[int]]) -> None:
        m,n = len(matrix),len(matrix[0])
        first_col_zero,first_row_zero= False,False
        for i in range(m):
            if matrix[i][0]==0:
                first_col_zero=True
                break
        for j in range(n):
            if matrix[0][j]==0:
                first_row_zero=True
                break
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0

        for i in range(1,m):
            if matrix[i][0]==0:
                for j in range(n):
                    matrix[i][j]=0

        for j in range(1,n):
            if matrix[0][j]==0:
                for i in range(m):
                    matrix[i][j]=0

        if first_row_zero:
            for j in range(n):
                matrix[0][j]=0
        if first_col_zero:
            for i in range(m):
                matrix[i][0]=0

# space (m+n). Time (m*n)
class Solution2:
    def setZeroes(self,matrix: List[List[int]]) -> None:
        m,n = len(matrix),len(matrix[0])
        rows,cols=[False]*m, [False]*n

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rows[i]=True
                    cols[j]=True

        for i in range(m):
            for j in range(n):
                if rows[i] or cols[j]:
                    matrix[i][j]=0


class MyTestCase(unittest.TestCase):
    def test1(self):
        matrix = [[1,1,1],
                  [1,0,1],
                  [1,1,1]]
        expected = [[1,0,1],
                    [0,0,0],
                    [1,0,1]]
        get_sol().setZeroes(matrix)
        self.assertEqual(expected, matrix)
    def test2(self):
        matrix = [[0,1,2,0],
                  [3,4,5,2],
                  [1,3,1,5]]
        expected = [[0,0,0,0],
                    [0,4,5,0],
                    [0,3,1,0]]
        get_sol().setZeroes(matrix)
        self.assertEqual(expected, matrix)
    def test3(self):
        matrix = [[ 1, 2, 3, 4],
                  [ 5, 0, 7, 8],
                  [ 0,10,11,12],
                  [13,14,15, 0]]
        expected =[[0,0,3,0],
                   [0,0,0,0],
                   [0,0,0,0],
                   [0,0,0,0]]
        get_sol().setZeroes(matrix)
        self.assertEqual(expected, matrix)
