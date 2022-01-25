from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M=10**9+7
        @cache
        def dfs(i,j):
            if i==m:
                return j==n
            if j==n:
                return 1
            res=0
            res+=dfs(i+1,j)
            res%=M

            if s[i]==t[j]:
                res+=dfs(i+1,j+1)
                res%=M
            return res

        m,n=len(s),len(t)
        return dfs(0,0)
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

class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(3,get_sol().numDistinct("rabbbit","rabbit"))
    def test02(self):
        self.assertEqual(5,get_sol().numDistinct("babgbag","bag"))
