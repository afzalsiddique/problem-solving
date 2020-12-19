from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = 0

        def traverse(row, col):
            if row < 0 or row >= m:
                return
            if col < 0 or col >= n:
                return

            if grid[row][col] == '1':
                grid[row][col] = '0'
                traverse(row, col+1)
                traverse(row, col-1)
                traverse(row+1, col)
                traverse(row-1, col)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    traverse(i, j)
                    cnt += 1
        return cnt
