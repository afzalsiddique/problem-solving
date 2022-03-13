from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    dp = []

    def canWinNim(self, n: int) -> bool:
        self.dp = [[-1] * (n + 1) for _ in range(2)]
        return self.helper(n, 1)

    # ID == 0 is opponent
    # ID ==1 is me
    def helper(self, n, ID):
        if n == 0:
            if ID == 1:
                return False
            return True
        if 1 <= n <= 3:
            if ID == 1:
                return True
            return False
        if self.dp[ID][n] != -1:
            return self.dp[ID][n]

        next = abs(ID - 1)
        if ID == 1: # if it is my turn
            self.dp[ID][n] = max(self.helper(n - 1, next), self.helper(n - 2, next), self.helper(n - 3, next))
        else: # if it is opponent's turn
            self.dp[ID][n] = min(self.helper(n - 1, next), self.helper(n - 2, next), self.helper(n - 3, next))
        return self.dp[ID][n]
class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        n = 1
        expected = True
        actual = solution.canWinNim(n)
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        n = 2
        expected = True
        actual = solution.canWinNim(n)
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        n = 3
        expected = True
        actual = solution.canWinNim(n)
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        n = 4
        expected = False
        actual = solution.canWinNim(n)
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        n = 5
        expected = True
        actual = solution.canWinNim(n)
        self.assertEqual(expected, actual)

    def test_6(self):
        solution = Solution()
        n = 8
        expected = False
        actual = solution.canWinNim(n)
        self.assertEqual(expected, actual)

