from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = {}
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        def helper(i,j):
            if i>=m or j>=n or i<0 or j<0:return 0
            if obstacleGrid[i][j]==1:return 0
            if (i,j) in dp:return dp[(i,j)]
            if i==m-1 and j==n-1:return 1
            dp[(i,j)] = helper(i+1,j) + helper(i,j+1)
            return dp[(i,j)]

        return helper(0,0)
    def uniquePathsWithObstacles_(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(0, m):
            for j in range(0, n):
                if i==0 and j==0:
                    continue
                elif obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[- 1][- 1]
