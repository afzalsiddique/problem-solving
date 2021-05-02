import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List



class Solution:
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
    def test1(self):
        s = "rabbbit"
        t = "rabbit"
        e = 3
        self.assertEqual(e,Solution().numDistinct(s,t))
    def test2(self):
        s = "babgbag"
        t = "bag"
        e = 5
        self.assertEqual(e,Solution().numDistinct(s,t))
