import unittest
from heapq import *
from typing import List

# binary search.  O(N∗log(max−min))
class Solution:
    # https://www.youtube.com/watch?v=G5wLN4UweAM
    # https://www.youtube.com/watch?v=oeQlc87HbbQ
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


# heap.time-> O(min(K,N)+K∗logN)
class Solution2:
    # https://www.youtube.com/watch?v=zIaMTdBQT34
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


