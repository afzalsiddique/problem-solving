import unittest
from collections import deque
from typing import List
def get_sol_obj(): return Solution()

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


class tester(unittest.TestCase):
    def test1(self):
        matrix = [
            [0,1,1,1],
            [1,1,1,1],
            [0,1,1,1]
        ]
        Output= 15
        self.assertEqual(Output,get_sol_obj().countSquares(matrix))
    def test2(self):
        matrix = [
            [1,0,1],
            [1,1,0],
            [1,1,0]
        ]
        Output= 7
        self.assertEqual(Output,get_sol_obj().countSquares(matrix))
