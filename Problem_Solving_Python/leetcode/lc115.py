from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dp(i:int,j:int):
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            res=0
            if s[i]==t[j]:
                res+=dp(i+1,j+1)
            res+=dp(i+1,j)
            return res

        return dp(0,0)
class Solution3:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dp(i,j):
            if i==len(s):
                return j==len(t)
            if j==len(t):
                return 1
            res=0
            res+=dp(i+1,j)

            if s[i]==t[j]:
                res+=dp(i+1,j+1)
            return res

        return dp(0,0)
class Solution2:
    def numDistinct(self, s: str, t: str) -> int:
        m,n=len(t),len(s)
        s='#'+s
        t='#'+t
        dp=[[0]*(n+1) for _ in range(m+1)]
        for j in range(n+1):
            dp[0][j]=1
        for i in range(1,m+1):
            dp[i][0]=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[j]==t[i]:
                    dp[i][j]=dp[i][j-1]+dp[i-1][j-1]
                else:
                    dp[i][j]=dp[i][j-1]
        return dp[-1][-1]

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(3,get_sol().numDistinct("rabbbit","rabbit"))
    def test02(self):
        self.assertEqual(5,get_sol().numDistinct("babgbag","bag"))
    def test03(self):
        self.assertEqual(3,get_sol().numDistinct("abbb","ab"))
