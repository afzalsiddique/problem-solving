from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()

# https://www.youtube.com/watch?v=MiqoA-yF-0M
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i,j):
            if j==len(word2):
                return len(word1)-i
            if i==len(word1):
                return len(word2)-j
            if word1[i]==word2[j]:
                return dp(i+1,j+1)
            return 1+min(dp(i+1,j),dp(i,j+1),dp(i+1,j+1))

        return dp(0,0)
class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        word1='#'+word1
        word2='#'+word2
        m,n=len(word1),len(word2)
        dp = [[0]*n for _ in range(m)]
        dp[0]=[i for i in range(n)]
        for i in range(m):
            dp[i][0]=i
        for i in range(1,m):
            for j in range(1,n):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        return dp[-1][-1]

class MyTestClass(unittest.TestCase):
    def test01(self):
        self.assertEqual(3,get_sol().minDistance("horse", "ros"))
    def test02(self):
        self.assertEqual(5,get_sol().minDistance("intention", "execution"))
    def test03(self):
        self.assertEqual(1,get_sol().minDistance("", "a"))
    # def test04(self):
