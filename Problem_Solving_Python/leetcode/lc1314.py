import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://computersciencesource.wordpress.com/2010/09/03/computer-vision-the-integral-image/
    def matrixBlockSum(self, mat, K):
        n = len(mat)
        m = len(mat[0])
        sums = defaultdict(int)

        for i in range(n):
            for j in range(m):
                sums[i,j] = sums[i-1,j] + sums[i,j-1] - sums[i-1,j-1] + mat[i][j]
        result = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                r1 = max(0, i-K)
                c1 = max(0, j-K)
                r2 = min(n-1, i+K)
                c2 = min(m-1, j+K)
                result[i][j] = sums[r2,c2] - sums[r2,c1-1] - sums[r1-1,c2] + sums[r1-1,c1-1]
        return result
class Solution2:
    # with dummy row and dummy col
    # https://computersciencesource.wordpress.com/2010/09/03/computer-vision-the-integral-image/
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # adding a dummy row and a dummy col
        no_row,no_col=len(mat),len(mat[0])
        for i in range(no_row):
            mat[i]=[0]+mat[i]
        mat=[[0]*(no_col+1)]+mat

        # main part
        m,n=len(mat),len(mat[0])
        dp = [[0]*(n) for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+mat[i][j]

        new_mat = [[0]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                r1,c1,r2,c2=max(0,i-k-1),max(0,j-k-1),min(m-1,i+k),min(n-1,j+k)
                new_mat[i][j]=dp[r2][c2]+dp[r1][c1]-dp[r2][c1]-dp[r1][c2]
        res = []
        for i in range(1,len(new_mat)):
            row=new_mat[i]
            res.append(row[1:])
        return res
class Solution3:
    # https://computersciencesource.wordpress.com/2010/09/03/computer-vision-the-integral-image/
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = dp[i][j+1]+dp[i+1][j]-dp[i][j]+mat[i][j]

        new_mat = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1,c1,r2,c2=max(0,i-k),max(0,j-k),min(m,i+k+1),min(n,j+k+1)
                new_mat[i][j]=dp[r2][c2]+dp[r1][c1]-dp[r2][c1]-dp[r1][c2]
        return new_mat


class tester(unittest.TestCase):
    def test_01(self):
        mat = [[1,2,3],[4,5,6],[7,8,9]]
        k = 1
        Output= [[12,21,16],[27,45,33],[24,39,28]]
        self.assertEqual(Output,get_sol().matrixBlockSum(mat,k))
    def test02(self):
        mat = [[1,2,3],[4,5,6],[7,8,9]]
        k = 2
        Output= [[45,45,45],[45,45,45],[45,45,45]]
        self.assertEqual(Output,get_sol().matrixBlockSum(mat,k))
    def test03(self):
        mat = [[5,2],[3,6]]
        k = 1
        Output= [[16,16],[16,16]]
        self.assertEqual(Output,get_sol().matrixBlockSum(mat,k))
    # def test_03(self):
    # def test_04(self):
    # def test_05(self):
    # def test_06(self):
    # def test_07(self):
    # def test_08(self):
