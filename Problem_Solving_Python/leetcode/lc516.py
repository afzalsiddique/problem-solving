from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution4:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dp(i,j):
            if i>j: return 0
            if i==j: return 1
            if s[i]==s[j]:
                return 2+dp(i+1,j-1)
            return max(dp(i+1,j),dp(i,j-1))

        return dp(0,len(s)-1)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def pali(s):
            n=len(s)
            if n==1:return 1
            if n==2:
                if s[0]==s[1]:return 2
                return 1
            if s in di:return di[s]
            if s[0]==s[-1]:
                di[s]= 2 + pali(s[1:-1])
            else:
                di[s] = max(pali(s[:-1]),pali(s[1:]))
            return di[s]


        di = {}
        return pali(s)


    def longestPalindromeSubseq_(self, s: str) -> int:
        n = len(s)
        dp = [[1] * n for _ in range(n)]
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 2
        for left in range(n - 1, -1, -1):
            for right in range(left + 2, n):
                if s[left] == s[right]:
                    dp[left][right] = dp[left + 1][right - 1] + 2
                else:
                    dp[left][right] = max(dp[left][right-1], dp[left+1][right])
        return dp[0][n-1]

    # to find actual palindrome (string)
    def longestPalindromeSubseq__(self, s: str) -> int:
        dp = {}
        def helper(s:str):
            n=len(s)
            if n==0:return ""
            if n==1:return s
            if n==2:
                if s[0]==s[1]:return s
                else:return s[0]
            if s in dp:return dp[s]
            if s[0]==s[-1]:
                return s[0] + helper(s[1:-1]) + s[-1]
            else:
                s1 = helper(s[:-1])
                s2 = helper(s[1:])
                if len(s1)>len(s2):
                    dp[s] = s1
                    return s1
                dp[s] = s2
                return s2

        return len(helper(s))


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(4, get_sol().longestPalindromeSubseq('bbbab'))
    def test02(self):
        self.assertEqual(2, get_sol().longestPalindromeSubseq('cbbd'))
    def test03(self):
        self.assertEqual(1, get_sol().longestPalindromeSubseq('abcdef'))
    def test04(self):
        self.assertEqual(3, get_sol().longestPalindromeSubseq('bbb'))
    def test05(self):
        self.assertEqual(4, get_sol().longestPalindromeSubseq('bbbb'))
    def test06(self):
        self.assertEqual(4, get_sol().longestPalindromeSubseq('qwertbbbbzxcv'))
    def test07(self):
        self.assertEqual(6, get_sol().longestPalindromeSubseq('qAwAeAAtAyAu'))
