# https://www.youtube.com/watch?v=MiqoA-yF-0M
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List



class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n= len(word1), len(word2)
        word1 = '#' + word1
        word2 = '#' + word2
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(n+1):
            dp[0][i] = i
        for j in range(m+1):
            dp[j][0] = j

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[-1][-1]