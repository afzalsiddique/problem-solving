# https://www.youtube.com/watch?v=CxrnOTUlNJE
import math
import unittest
from typing import List



class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n,fresh_orange=len(grid),len(grid[0]),False
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh_orange = True
                    break
        if not fresh_orange:return 0

        q,day = [],0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((day,i,j))

        while q:
            day,i,j= q.pop(0)
            grid[i][j]=3 # 3 indicates visited
            if i>0 and grid[i-1][j]==1:
                q.append((day+1,i-1,j))
                grid[i-1][j]=3
            if i+1<m and grid[i+1][j]==1:
                q.append((day+1, i+1,j))
                grid[i+1][j]=3
            if j>0 and grid[i][j-1]==1:
                q.append((day+1,i,j-1))
                grid[i][j-1]=3
            if j+1<n and grid[i][j+1]==1:
                q.append((day+1, i,j+1))
                grid[i][j+1]=3

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return day

class MyTestCase(unittest.TestCase):
    def test_1(self):
        grid = [[2,1,1],[1,1,0],[0,1,1]]
        actual = Solution().orangesRotting(grid)
        expected = 4
        self.assertEqual(expected,actual)
    def test_2(self):
        grid = [[2,1,1],[0,1,1],[1,0,1]]
        actual = Solution().orangesRotting(grid)
        expected = -1
        self.assertEqual(expected,actual)
    def test_3(self):
        grid = [[0,2]]
        actual = Solution().orangesRotting(grid)
        expected = 0
        self.assertEqual(expected,actual)
    def test_4(self):
        grid = [[2,2],[1,1],[0,0],[2,0]]
        actual = Solution().orangesRotting(grid)
        expected = 1
        self.assertEqual(expected,actual)
