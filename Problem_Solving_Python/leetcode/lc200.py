import unittest
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        ans = 0
        def dfs(x,y):
            if x>=m or y>=n or x<0 or y<0:return
            if grid[x][y]=='0':return
            grid[x][y]='0'
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(x+dx,y+dy)
            return
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    dfs(i,j)
                    ans+=1
        return ans
class tester(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        actual = solution.numIslands(grid)
        expected = 1
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        actual = solution.numIslands(grid)
        expected = 3
        self.assertEqual(expected, actual)
