from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(0,n):
            trail = [0] * (n-i-1)
            triangle[i] += trail
        dp = [[-1]*n for _ in range(n)]
        def helper(traingle, row, col, dp):
            n = len(triangle)
            if row==n-1:
                return triangle[row][col]
            if dp[row][col] != -1:
                return dp[row][col]
            bottom = helper(traingle, row+1, col, dp)
            bottom_right = helper(triangle, row+1, col+1, dp)
            dp[row][col] = triangle[row][col] + min(bottom, bottom_right)
            return dp[row][col]

        return helper(triangle, 0, 0, dp)
