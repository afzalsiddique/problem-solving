from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution2()
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
        for left in range(n-1, -1, -1):
            for right in range(left+2,n):
                if s[left] == s[right] and dp[left+1][right-1]:
                    dp[left][right] = True
        return sum(sum(x) for x in dp)

class Solution2:
    def countSubstrings(self, s: str) -> int:
        @cache
        def isPalindrome(i,j):
            if i>j: return True
            # if i==j: return True # not required
            if s[i]!=s[j]: return False
            return isPalindrome(i+1,j-1)

        n=len(s)
        res=0
        for i in range(n):
            for j in range(i+1,n): # return res+len(s)
            # for j in range(i,n): # return res
                res+=isPalindrome(i,j)
        return res+len(s)
        # return res
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(9, get_sol().countSubstrings('babbcb'))
    def test02(self):
        self.assertEqual(3, get_sol().countSubstrings("abc"))
    def test03(self):
        self.assertEqual(6, get_sol().countSubstrings("aaa"))
    def test04(self):
        self.assertEqual(16, get_sol().countSubstrings("bbbabbb"))
    def test05(self):
        self.assertEqual(9, get_sol().countSubstrings("abbba"))
