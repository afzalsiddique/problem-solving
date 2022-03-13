from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution:
    # https://www.youtube.com/watch?v=xFv_Hl4B83A&t=529s
    def totalNQueens(self, n: int) -> int:
        res = []
        queens = [-1] * n
        # queens is a one-dimension array, like [1, 3, 0, 2] means
        # [.Q..]
        # [...Q]
        # [Q...]
        # [..Q.]
        # index represents row no and value represents col no

        def dfs(index):
            if index == len(queens): # n queens have been placed correctly
                res.append(queens[:])
                return  # backtracking
            for i in range(len(queens)):
                queens[index] = i
                if valid(index):  # pruning
                    dfs(index + 1, )

        # check whether nth queens can be placed
        def valid(n):
            for i in range(n):
                if abs(queens[i] - queens[n]) == n - i:  # same digonal
                    return False
                if queens[i] == queens[n]:  # same column
                    return False
            return True


        dfs(0)
        return len(res)


class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = solution.totalNQueens(4)
        expected = 2
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        actual = solution.totalNQueens(5)
        expected = 10
        self.assertEqual(expected, actual)



