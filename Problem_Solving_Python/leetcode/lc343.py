from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def dp(left):
            if left<0:
                return float('-inf')
            if left==0:
                return 1
            res=float('-inf')
            for i in range(1,left+1):
                res=max(res, i*dp(left - i))
            return res

        if n==2: return 1
        if n==3: return 2
        return dp(n)
class Solution3:
    def integerBreak(self, n: int) -> int:
        di={}
        def helper(n):
            if n==1 or n==2: return 1
            if n==3: return 2
            if n in di: return di[n]
            result=0
            for i in range(2,n):
                a=i
                b=n-a
                if a>b:break
                result=max(result,a*helper(b),a*b)
            di[n]=result
            return di[n]

        return helper(n)
class Solution2:
    def integerBreak(self, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(n+1)]
        dp[0] = [1 for _ in range(n+1)]
        for row in dp:
            row[0] = 1
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(1, n+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-i]*i)
        return dp[n][n]
class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(1,get_sol().integerBreak(1))
    def test2(self):
        self.assertEqual(1,get_sol().integerBreak(2))
    def test3(self):
        self.assertEqual(2,get_sol().integerBreak(3))
    def test4(self):
        self.assertEqual(4,get_sol().integerBreak(4))
    def test5(self):
        self.assertEqual(6,get_sol().integerBreak(5))
    def test6(self):
        self.assertEqual(9,get_sol().integerBreak(6))
    def test7(self):
        self.assertEqual(36,get_sol().integerBreak(10))
    def test8(self):
        self.assertEqual(18,get_sol().integerBreak(8))
    def test9(self):
        self.assertEqual(4374,get_sol().integerBreak(23))
