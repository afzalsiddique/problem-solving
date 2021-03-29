from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List

class Solution:
    # https://www.youtube.com/watch?v=l3hda49XcDE
    def isMatch(self, s: str, p: str) -> bool:
        s='#'+s
        p='#'+p
        m,n=len(s),len(p)
        dp = [[False]*n for _ in range(m)]
        dp[0][0]= True
        for i in range(1,m):
            dp[i][0]=False
        for j in range(1,n):
            if p[j]=='*':
                dp[0][j]=dp[0][j-2]
        for i in range(1,m):
            for j in range(1,n):
                if s[i]==p[j] or p[j]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j]=='*':
                    dp[i][j] = dp[i][j-2]
                    if s[i]==p[j-1] or p[j-1]=='.':
                        dp[i][j]=dp[i][j] or dp[i-1][j]
        return dp[-1][-1]


# class mytestcase(unittest.TestCase):
#     def test1(self):
#         self.assertEqual(False, Solution().isMatch( s= "aa", p = "a"))
#     def test2(self):
#         self.assertEqual(True, Solution().isMatch(s = "aa", p = "*"))
#     def test3(self):
#         self.assertEqual(False, Solution().isMatch(s = "cb", p = "?a"))
#     def test4(self):
#         self.assertEqual(True, Solution().isMatch(s = "adceb", p = "*a*b"))
#     def test5(self):
#         self.assertEqual(False, Solution().isMatch(s = "acdcb", p = "a*c?b"))
#     def test6(self):
#         self.assertEqual(True, Solution().isMatch(s = "", p = ""))
#     def test7(self):
#         self.assertEqual(False, Solution().isMatch(s = "ab", p = ""))
#     def test8(self):
#         self.assertEqual(True, Solution().isMatch(s = "", p = "*"))
#     def test9(self):
#         self.assertEqual(False, Solution().isMatch(s = "", p = "q"))
