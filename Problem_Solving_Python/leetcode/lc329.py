from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List








class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        di = {}
        def dfs(row,col,prev):
            if row>=m or col>=n or row<0 or col<0:return 0
            if matrix[row][col]<=prev:return 0
            if (row,col) in di:
                return di[(row,col)]
            ans,temp = 1,0
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                i,j = row+dx,col+dy
                temp = max(temp,dfs(i,j,matrix[row][col]))
            di[(row,col)] = ans+temp
            return di[(row,col)]
        ans = 1
        for i in range(m):
            for j in range(n):
                ans = max(ans,dfs(i,j,float('-inf')))
        return ans


class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        self.assertEqual(4, solution.longestIncreasingPath( [[9,9,4],[6,6,8],[2,1,1]]))

    def test_2(self):
        solution = Solution()
        self.assertEqual(4, solution.longestIncreasingPath( [[3,4,5],[3,2,6],[2,2,1]]))

    def test_3(self):
        solution = Solution()
        self.assertEqual(1, solution.longestIncreasingPath( [[1]]))
