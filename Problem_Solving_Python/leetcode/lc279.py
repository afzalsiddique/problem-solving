from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution3()
# https://www.youtube.com/watch?v=1xfx6M_GqFk
class Solution3:
    def numSquares(self, n: int) -> int:
        di = {}
        def helper(n):
            if n<=3:
                return n
            if n in di:
                return di[n]
            minn = float('inf')
            i = 1
            while i*i<=n:
                temp = helper(n-i*i)
                minn = min(minn, temp)
                i+=1
            di[n] = minn+1
            return di[n]
        return helper(n)
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [x for x in range(n + 1)]
        dp[0] = float('inf')
        for num in range(4, n + 1):
            minn = float('inf')
            i = 1
            while i * i <= num:
                if i * i == num:
                    minn = 1
                else:
                    minn = min(minn, dp[num - i * i] + 1)
                i += 1
            dp[num] = minn
        return dp[-1]


class Solution2:
    def numSquares(self, n: int) -> int:
        dp = [x for x in range(n + 1)]
        for num in range(1, n + 1):
            i = 1
            while i * i <= num:
                sq = i*i
                dp[num] = min(dp[num], 1+dp[num-sq])
                i += 1
        return dp[-1]
class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, get_sol().numSquares(12))
    def test_2(self):
        self.assertEqual(2, get_sol().numSquares(13))
    def test_3(self):
        self.assertEqual(1, get_sol().numSquares(1))
    def test_4(self):
        self.assertEqual(1, get_sol().numSquares(4))
    def test_5(self):
        self.assertEqual(2, get_sol().numSquares(5))
    def test_6(self):
        self.assertEqual(3, get_sol().numSquares(6110))
