import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        word1='#'+word1
        word2='#'+word2
        dp=[[None]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j]=j
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=1+min(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]


class tester(unittest.TestCase):
    def test01(self):
        word1 = "sea"
        word2 = "eat"
        Output= 2
        self.assertEqual(Output, get_sol().minDistance(word1,word2))
    def test02(self):
        word1 = "leetcode"
        word2 = "etco"
        Output= 4
        self.assertEqual(Output, get_sol().minDistance(word1,word2))