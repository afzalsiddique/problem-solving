# https://www.youtube.com/watch?v=MiqoA-yF-0M
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List



class Solution:
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
    def test_1(self):
        self.assertEqual(3,Solution().minDistance("horse", "ros"))
