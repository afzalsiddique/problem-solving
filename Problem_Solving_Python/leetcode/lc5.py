import math
import unittest
from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i]=True
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1] = True
        for i in reversed(range(n-2)):
            for j in range(i+1,n):
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
        length = 0
        pal = ""
        for i in reversed(range(n)):
            for j in range(i,n):
                if dp[i][j]==True and j-i+1>length:
                    length = j-i+1
                    pal = s[i:j+1]
        return pal

class Case(unittest.TestCase):
    def test_1(self):
        s = 'babad'
        ac = Solution().longestPalindrome(s)
        self.assertEqual('aba',ac)
    def test_2(self):
        s = 'a'
        ac = Solution().longestPalindrome(s)
        ex = 'a'
        self.assertEqual(ex,ac)
    def test_3(self):
        s = 'aa'
        ac = Solution().longestPalindrome(s)
        ex = 'aa'
        self.assertEqual(ex,ac)
    def test_4(self):
        s = 'aaa'
        ac = Solution().longestPalindrome(s)
        ex = 'aaa'
        self.assertEqual(ex,ac)
    def test_5(self):
        s = "abacab"
        ac = Solution().longestPalindrome(s)
        ex = 'bacab'
        self.assertEqual(ex,ac)


