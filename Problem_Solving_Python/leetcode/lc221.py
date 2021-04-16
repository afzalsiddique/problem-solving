from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
    # https://www.youtube.com/watch?v=RElcqtFYTm0
        m,n=len(matrix),len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1]=='1':
                    dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        ans = max(map(max,dp)) # max val in a matrix
        return ans*ans
# dfs + memo
class Solution2:
    res = 0
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dp = {}
        def dfs(r,c):
            if r==m-1 or c==n-1:
                return 0 if matrix[r][c]=='0' else 1
            if matrix[r][c]=='0':return 0
            if (r,c) in dp:return dp[(r,c)]
            down = dfs(r+1,c)
            right = dfs(r,c+1)
            down_right = dfs(r+1,c+1)
            minn = min(down,right,down_right)
            area = 1+minn if minn>0 else 1
            dp[(r,c)] = area
            self.res = max(self.res,area)
            return dp[(r,c)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    self.res = max(self.res,1)
                dfs(i,j)
        return self.res*self.res




class mycase(unittest.TestCase):
    def test1(self):
        self.assertEqual(4,Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    def test2(self):
        self.assertEqual(1,Solution().maximalSquare([["0","1"],["1","0"]]))
    def test3(self):
        self.assertEqual(0,Solution().maximalSquare([["0"]]))
    # def test4(self):
    # def test5(self):


# class mycase(unittest.TestCase):
#     def test1(self):
#         self.assertEqual('BANC', Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))
#     def test2(self):
#         self.assertEqual('a', Solution().minWindow(s = "a", t = "a"))
#     def test3(self):
#         self.assertEqual('', Solution().minWindow(s = "a", t = "b"))

