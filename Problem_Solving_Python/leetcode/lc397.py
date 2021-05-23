import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    def integerReplacement(self, n: int) -> int:
        dp = {}
        def dfs(n):
            if n==1: return 0
            if n==0: return float('inf')
            if n in dp: return dp[n]
            if n%2==0:
                ans=1+dfs(n//2)
            else:
                ans=1+min(dfs(n+1),dfs(n-1))
            dp[n]=ans
            return ans

        return dfs(n)

class tester(unittest.TestCase):
    def test01(self):
        n = 8
        Output= 3
        self.assertEqual(Output, get_sol().integerReplacement(n))
    def test02(self):
        n = 7
        Output= 4
        self.assertEqual(Output, get_sol().integerReplacement(n))
    def test03(self):
        n = 4
        Output= 2
        self.assertEqual(Output, get_sol().integerReplacement(n))
