import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        self.initialize(mat)
        res=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j]=self.sumRegion(i-k,j-k,i+k,j+k)
        return res
    def initialize(self, mat: List[List[int]]):
        self.mat=mat
        m,n= len(mat), len(mat[0])
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                mat[i][j]+=mat[i+1][j] if i+1<m else 0
                mat[i][j]+=mat[i][j+1] if j+1<n else 0
                mat[i][j]-=mat[i+1][j+1] if i+1<m and j+1<n else 0
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int: # range-sum-query-2d-immutable. leetcode 304
        mat=self.mat
        m,n=len(mat),len(mat[0])
        row1=max(0,row1); col1=max(0,col1); row2=min(m-1,row2); col2=min(n-1,col2)
        m,n= len(mat), len(mat[0])
        res=mat[row1][col1]
        res-=mat[row2+1][col1] if row2+1<m else 0
        res-=mat[row1][col2+1] if col2+1<n else 0
        res+=mat[row2+1][col2+1] if row2+1<m and col2+1<n else 0
        return res
class Solution4:
    # https://computersciencesource.wordpress.com/2010/09/03/computer-vision-the-integral-image/
    def matrixBlockSum(self, mat, K):
        m = len(mat)
        n = len(mat[0])
        sums = defaultdict(int)

        for i in range(m):
            for j in range(n):
                sums[i,j] = sums[i-1,j] + sums[i,j-1] - sums[i-1,j-1] + mat[i][j]
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1 = max(0, i-K)
                c1 = max(0, j-K)
                r2 = min(m-1, i+K)
                c2 = min(n-1, j+K)
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

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual([[12,21,16],[27,45,33],[24,39,28]],get_sol().matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]],1))
    def test02(self):
        self.assertEqual([[45,45,45],[45,45,45],[45,45,45]],get_sol().matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]],2))
    def test03(self):
        self.assertEqual([[16,16],[16,16]],get_sol().matrixBlockSum([[5,2],[3,6]],1))
    def test04(self):
        self.assertEqual([[731, 731, 731], [930, 930, 930], [930, 930, 930], [930, 930, 930], [721, 721, 721]],get_sol().matrixBlockSum([[67,64,78],[99,98,38],[82,46,46],[6,52,55],[55,99,45]], 3))
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
