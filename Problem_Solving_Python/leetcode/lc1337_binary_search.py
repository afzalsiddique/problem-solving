import heapq
from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        # find no of ones using binary search
        # n = 5
        #
        # a = [1, 1, 0, 0, 0]
        # ans = n - bisect_left(a[::-1], 1)
        # print(ans) # 2
        #
        # a = [0, 0, 0, 0, 0]
        # ans = n - bisect_left(a[::-1], 1)
        # print(ans) # 0
        #
        # a = [1, 1, 1, 1, 1]
        # ans = n - bisect_left(a[::-1], 1)
        # print(ans) # 5

        n=len(mat)
        tuples = [(n-bisect_left(mat[row_no][::-1], 1), row_no) for row_no in range(n)]
        tuples.sort() # tuples will be sorted based on no of ones then row no
        return [tuples[i][1] for i in range(k)]




import unittest
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        self.assertEqual([2,0,3], solution.kWeakestRows(mat =
                                                        [[1,1,0,0,0],
                                                         [1,1,1,1,0],
                                                         [1,0,0,0,0],
                                                         [1,1,0,0,0],
                                                         [1,1,1,1,1]],
                                                        k = 3))

    def test_2(self):
        solution = Solution()
        self.assertEqual([0,2], solution.kWeakestRows(mat =
                                                            [[1,0,0,0],
                                                             [1,1,1,1],
                                                             [1,0,0,0],
                                                             [1,0,0,0]],
                                                            k = 2))