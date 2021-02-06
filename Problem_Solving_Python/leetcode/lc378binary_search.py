# https://www.youtube.com/watch?v=oeQlc87HbbQ
import unittest
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[n - 1][n - 1]
        while lo < hi:
            mid = (lo + hi) // 2
            if self.get_less_than_or_smaller(mid, matrix) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def get_less_than_or_smaller(self, num, matrix):
        n = len(matrix)
        cnt = 0
        row = 0
        col = n - 1
        while row < n and col >= 0:
            if matrix[row][col] <= num:
                cnt += col + 1
                row += 1
            else:
                col -= 1
        return cnt


class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = 13
        actual = sol.kthSmallest(matrix=[
            [1, 5, 9],
            [10, 11, 13],
            [12, 13, 15]
        ],
            k=8)
        self.assertEqual(expected, actual)


