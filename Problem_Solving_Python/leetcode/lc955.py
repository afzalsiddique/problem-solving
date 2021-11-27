import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        m, n = len(A), len(A[0])
        ans, in_order = 0, [False] * (m-1)
        for j in range(n):
            tmp_in_order = in_order[:]
            for i in range(m-1):
                # previous step, rows are not in order; and current step rows are not in order, remove this column
                if not in_order[i] and A[i][j] > A[i+1][j]:
                    ans += 1; break
                # previous step, rows are not in order, but they are in order now
                elif A[i][j] < A[i+1][j] and not in_order[i]:
                    tmp_in_order[i] = True
            # if column wasn't removed, update the row order information
            else: in_order = tmp_in_order
            # not necessary, but speed things up
            if all(in_order): return ans
        return ans


class MyTestCase(unittest.TestCase):
    def test1(self):
        strs = ["ca","bb","ac"]
        Output= 1
        self.assertEqual(Output, get_sol().minDeletionSize(strs))
    def test2(self):
        strs = ["xc","yb","za"]
        Output= 0
        self.assertEqual(Output, get_sol().minDeletionSize(strs))
    def test3(self):
        strs = ["zyx","wvu","tsr"]
        Output= 3
        self.assertEqual(Output, get_sol().minDeletionSize(strs))
    def test4(self):
        strs = ["zyxwvu","abcdef","adfksha"]
        Output= 6
        self.assertEqual(Output, get_sol().minDeletionSize(strs))
    def test5(self):
        strs = ["xga","xfb","yfa"]
        Output= 1
        self.assertEqual(Output, get_sol().minDeletionSize(strs))
    # def test6(self):
    # def test7(self):
