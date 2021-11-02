import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
from math import factorial
def get_sol(): return Solution()
class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = {}
        def f(n,k):
            if n==1: return k
            if k==1: return 1
            if (n,k) in dp: return dp[n,k]
            dp[n,k] = sum(f(n-1,k) for k in range(1,k+1))
            return dp[n,k]

        return f(n,5)

class Solution2:
    # https://leetcode.com/problems/count-sorted-vowel-strings/discuss/1021180/Python-Start-and-bars-explained
    def countVowelStrings(self, n: int) -> int:
        return int(factorial(n+4) / factorial(n) /factorial(4))

class MyTestCase(unittest.TestCase):
    def test1(self):
        n = 1
        Output= 5
        self.assertEqual(Output, get_sol().countVowelStrings(n))
    def test2(self):
        n = 2
        Output= 15
        self.assertEqual(Output, get_sol().countVowelStrings(n))
    def test3(self):
        n = 33
        Output= 66045
        self.assertEqual(Output, get_sol().countVowelStrings(n))
    # def test4(self):
    # def test5(self):
    # def test6(self):
