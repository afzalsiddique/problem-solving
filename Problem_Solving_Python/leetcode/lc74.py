#*** same as 240 ***
import unittest
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n-1
        while row<m and col >=0:
            if target==matrix[row][col]:
                return True
            if target < matrix[row][col]:
                col-=1
            else:
                row+=1
        return False

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = False
        actual = sol.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20)
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = True
        actual = sol.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5)
        self.assertEqual(expected, actual)