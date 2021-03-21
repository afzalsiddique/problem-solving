# https://www.youtube.com/watch?v=MiqoA-yF-0M
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List



class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m=len(grid)
        if not m:return 0
        n=len(grid[0])
        def dfs(row,col):
            if row>=m or col>=n or row<0 or col<0:return 0
            if grid[row][col]==0:return 0
            ans = grid[row][col]
            prev_value = grid[row][col]
            grid[row][col]=0
            temp = float('-inf')
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                i,j=row+dr,col+dc
                temp = max(temp,dfs(i,j))
            grid[row][col]=prev_value
            return ans+temp

        maxx = float('-inf')
        for i in range(m):
            for j in range(n):
                maxx=max(maxx, dfs(i,j))
        return maxx

grid = [[0,6,0],
     [5,8,7],
     [0,9,0]]
print('e:24', Solution().getMaximumGold(grid))
grid = [[1,0,7],
     [2,0,6],
     [3,4,5],
     [0,3,0],
     [9,0,20]]
print('e:28', Solution().getMaximumGold(grid))