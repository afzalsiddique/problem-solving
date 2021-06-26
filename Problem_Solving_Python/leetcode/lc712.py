import itertools;
import math;
import operator;
import random;
from bisect import *;
from collections import deque, defaultdict, Counter, OrderedDict;
from heapq import *;
import unittest;
from typing import List;


def get_sol(): return Solution()


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = {}

        def lcs(i,j):  # longest common subsequence
            if i >= m or j >= n: return 0
            if (i,j) in dp: return dp[i,j]
            if s1[i] == s2[j]:
                ans = ord(s1[i]) + lcs(i+1,j+1)
            else:
                ans = max(lcs(i+1,j), lcs(i,j+1))
            dp[i, j] = ans
            return ans

        ans = lcs(0, 0)
        return sum(map(ord, s1 + s2)) - 2*ans


class tester(unittest.TestCase):
    def test1(self):
        s1 = "sea"
        s2 = "eat"
        Output = 231
        self.assertEqual(Output, Solution().minimumDeleteSum(s1, s2))

    def test2(self):
        s1 = "delete"
        s2 = "leet"
        Output = 403
        self.assertEqual(Output, Solution().minimumDeleteSum(s1, s2))

    def test3(self):
        s1 = "ccaccjp"
        s2 = "fwosarcwge"
        Output = 1399
        self.assertEqual(Output, Solution().minimumDeleteSum(s1, s2))
    # def test4(self):
    #     self.assertEqual(Output,Solution().minimumDeleteSum(s1,s2))
    # def test5(self):
    #     self.assertEqual(Output,Solution().minimumDeleteSum(s1,s2))
