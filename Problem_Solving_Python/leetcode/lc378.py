from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
# from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution:
    # binary search.  O(N∗log(max−min))
    # https://www.youtube.com/watch?v=G5wLN4UweAM
    # https://www.youtube.com/watch?v=oeQlc87HbbQ
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        lo, hi = mat[0][0], mat[-1][-1]
        while lo <= hi: # group1
            # while lo < hi: # group2
            mid = (lo + hi) // 2
            if self.get_less_than_or_smaller(mid, mat) < k:
                lo = mid + 1
            else:
                hi=mid-1 # group1
                # hi=mid # group2
        return lo

    def get_less_than_or_smaller(self, num, mat):
        # one liner
        # return sum(bisect_right(row,num) for row in matrix)

        n = len(mat)
        cnt = 0
        row = 0
        col = n - 1
        while row < n and col >= 0:
            if mat[row][col] <= num:
                cnt += col + 1
                row += 1
            else:
                col -= 1
        return cnt


class Solution2:
    # heap.time-> O(min(K,N)+K∗logN)
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
    def test01(self):
        self.assertEqual(13, get_sol().kthSmallest([ [1, 5, 9], [10, 11, 13], [12, 13, 15] ], 8))
    def test02(self):
        self.assertEqual(1, get_sol().kthSmallest([[1,2],[1,3]], 2))
    def test03(self):
        self.assertEqual(1, get_sol().kthSmallest([[1,2],[1,3]], 1))
    def test04(self):
        self.assertEqual(2, get_sol().kthSmallest([[1,4],[2,5]], 2))
    def test05(self):
        self.assertEqual(14, get_sol().kthSmallest([[1,3,5],[6,7,12],[11,14,14]], 8))
