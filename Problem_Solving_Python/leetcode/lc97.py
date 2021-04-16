import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List


class Solution:
    # https://leetcode.com/problems/interleaving-string/discuss/31879/My-DP-solution-in-C%2B%2B
    def isInterleave(self, s1, s2, s3):
        m,n,l=len(s1),len(s2),len(s3)
        if l!=m+n: return False
        s1,s2,s3='#'+s1,'#'+s2,'#'+s3
        dp=[[False]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 and j==0:
                    dp[i][j]=True
                elif i==0:
                    dp[i][j]=(dp[i][j-1] and s2[j]==s3[i+j])
                elif j==0:
                    dp[i][j]=(dp[i-1][j] and s1[i]==s3[i+j])
                else:
                    dp[i][j]=(dp[i-1][j] and s1[i]==s3[i+j]) or (dp[i][j-1] and s2[j]==s3[i+j])
        return dp[-1][-1]

    # WA.
    def isInterleave3(self, s1, s2, s3):
        m,n,l=len(s1),len(s2),len(s3)
        if l!=m+n: return False
        if m==0: return s2==s3
        if n==0: return s1==s3
        s1='#'+s1
        s2='#'+s2
        s3='#'+s3
        dp=[[False]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0]=True
        for j in range(n+1):
            dp[0][j]=True
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i]==s3[i+j] :
                    dp[i][j]=dp[i-1][j]
                elif s2[j]==s3[i+j]:
                    dp[i][j]=dp[i][j-1]
        return dp[-1][-1]


# brute force. time: 2^(m+n) space: m+n
class Solution2:
    def isInterleave(self, s1, s2, s3):
        def helper(s1,i,s2,j,res,s3):
            if res==s3 and i==len(s1) and j==len(s2):
                return True
            ans=False
            if i<len(s1):
                ans|=helper(s1,i+1,s2,j,res+s1[i],s3)
            if j<len(s2):
                ans|=helper(s1,i,s2,j+1,res+s2[j],s3)
            return ans

        if len(s1)+len(s2)!=len(s3): return False
        return helper(s1,0,s2,0,"",s3)
# class Solution: # 100%
#     def isInterleave(self, s1, s2, s3):
#         if len(s1) + len(s2) != len(s3):
#             return False
#         i, j, p = 0, 0, 0 # i, j, p are pointers for s1, s2 and s3
#         while i >= 0 and j < len(s2):
#             if i < len(s1) and s3[p] == s1[i]: # always choose the first string
#                 i, p = i + 1, p + 1
#             elif s3[p] == s2[j]: # if the first string doesn't match, we choose the second string
#                 j, p = j + 1, p + 1
#             else: # if choosing the first string was wrong in previous steps, we retro
#                 i, j = i - 1, j + 1
#         return s1[i:] + s2[j:] == s3[p:] and i >= 0

class tester(unittest.TestCase):
    def test1(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
        Output= True
        self.assertEqual(Output,Solution().isInterleave(s1,s2,s3))
    def test2(self):
        s1 = ""
        s2 = ""
        s3 = "a"
        Output= False
        self.assertEqual(Output,Solution().isInterleave(s1,s2,s3))
    def test3(self):
        s1 = "cabbcaaacacbac"
        s2 = "acabaabacabcca"
        s3 = "cacabaabacaabccbabcaaacacbac"
        Output= True
        self.assertEqual(Output,Solution().isInterleave(s1,s2,s3))
    def test4(self):
        s1 = "a"
        s2 = ""
        s3 = "c"
        Output= False
        self.assertEqual(Output,Solution().isInterleave(s1,s2,s3))
    def test5(self):
        s1 = "a"
        s2 = ""
        s3 = "a"
        Output= True
        self.assertEqual(Output,Solution().isInterleave(s1,s2,s3))
    def test6(self):
        s1 = "db"
        s2 = "b"
        s3 = "cbb"
        Output= False
        self.assertEqual(Output,Solution().isInterleave(s1,s2,s3))
