import unittest
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        dp = [[0]*(n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    dp[i][j]=0
                else:
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        total = sum(sum(row) for row in dp)
        return total

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        matrix = [
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
        ]
        expected = 30
        actual = solution.countSquares(matrix)
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        matrix = [
            [1, 0, 1],
            [1, 1, 0],
            [1, 1, 0]
        ]
        expected = 7
        actual = solution.countSquares(matrix)
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        matrix = [
            [0,1,1,1],
            [1,1,1,1],
            [0,1,1,1]
        ]
        expected = 15
        actual = solution.countSquares(matrix)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
