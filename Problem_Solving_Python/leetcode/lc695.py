import unittest
from random import randrange
from typing import List



class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n:return 0
            if grid[i][j]==0:return 0
            grid[i][j]=0
            cnt = 1
            cnt += dfs(i+1,j)
            cnt+=dfs(i-1,j)
            cnt+=dfs(i,j+1)
            cnt+=dfs(i,j-1)
            return cnt

        maxx=0
        for i in range(m):
            for j in range(n):
                maxx=max(maxx, dfs(i,j))
        return maxx
