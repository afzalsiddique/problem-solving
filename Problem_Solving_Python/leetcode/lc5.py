import math
import unittest
from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        maxx,txt=float('-inf'),""
        for i in range(n):
            dp[i][i]=1
            txt = s[i:i+1]
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1] = 1
                txt = s[i:i+2]
        for i in reversed(range(n-2)):
            for j in range(i+2, n):
                a = s[i:j+1] # debugging
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=1
                    if j-i+1>maxx:
                        txt = s[i:j+1]
                        maxx = max(maxx,j-i+1)
        return txt

class Case(unittest.TestCase):
    def test_1(self):
        s = 'babad'
        ac = Solution().longestPalindrome(s)
        ex = 'bab'
        self.assertEqual(ex,ac)
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


