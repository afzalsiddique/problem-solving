# https://www.youtube.com/watch?v=zIaMTdBQT34
from heapq import *
import unittest
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []
        for j in range(n):
            heappush(min_heap, (matrix[0][j],0,j)) # val, row, col
        for i in range(k-1):
            tup = heappop(min_heap)
            if tup[1]==n-1: # last row. next row is invalid
                continue
            row,col = tup[1]+1, tup[2]
            val = matrix[row][col]
            heappush(min_heap, (val, row, col))
        return heappop(min_heap)[0]


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

    def test_2(self):
        sol = Solution()
        expected = 1
        actual = sol.kthSmallest([[1,2],[1,3]], 2)
        self.assertEqual(expected, actual)


