import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/sort-the-matrix-diagonally/discuss/489749/JavaPython-Straight-Forward
    def diagonalSort(self, mat):
        n, m = len(mat), len(mat[0])
        di = defaultdict(list)
        for i in range(n):
            for j in range(m):
                di[i - j].append(mat[i][j])
        for k in di:
            di[k].sort(reverse=True)
        for i in range(n):
            for j in range(m):
                mat[i][j] = di[i - j].pop()
        return mat
class Solution2:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        def sort_diagonal(row,col): # starting row, starting col
            diagonal=[]
            r,c=row,col
            while r<m and c<n:
                diagonal.append(mat[r][c])
                r+=1
                c+=1
            diagonal.sort()
            r,c=row,col
            for x in diagonal:
                mat[r][c]=x
                r+=1
                c+=1

        sort_diagonal(0,0)
        for i in range(1,m):
            sort_diagonal(i,0)
        for j in range(1,n):
            sort_diagonal(0,j)
        return mat
class tester(unittest.TestCase):
    def test1(self):
        mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
        Output= [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
        self.assertEqual(Output,Solution().diagonalSort(mat))
    def test2(self):
        mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
        Output= [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
        self.assertEqual(Output,Solution().diagonalSort(mat))
