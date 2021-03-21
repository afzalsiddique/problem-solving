import unittest
from random import randrange
from typing import List



class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        def dfs(row, col):
            if row<0 or col<0 or row>=m or col>=n:return 0
            if grid[row][col]==0:return 0
            grid[row][col]=0
            area = 1
            for (dr,dc) in [(1,0),(-1,0),(0,1),(0,-1)]:
                i,j = row + dr, col + dc
                area+= dfs(i,j)
            return area

        maxx=0
        for i in range(m):
            for j in range(n):
                maxx=max(maxx, dfs(i,j))
        return maxx

    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        def dfs(r,c):
            if grid[r][c]==0:return 0
            area = 1
            grid[r][c]=0
            for (dr,dc) in [(1,0),(-1,0),(0,1),(0,-1)]:
                i = r+dr
                j = c+dc
                if i<m and j<n and i>=0 and j >=0 and grid[i][j]==1:
                    area += dfs(i,j)
            return area

        max_area = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    area = dfs(r,c)
                    max_area=max(max_area, area)
        return max_area
