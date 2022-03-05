from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution6:
    # because dp table only accesses the prev row and the prev col, we can have 1d dp
    # memory O(len(s2)) time O(m*n)
    def isInterleave(self, s1, s2, s3):
        m,n,l=len(s1),len(s2),len(s3)
        if l!=m+n: return False
        s1,s2,s3='#'+s1,'#'+s2,'#'+s3
        dp=[False]*(n+1)
        for i in range(m+1):
            for j in range(n+1):
                if i==0 and j==0: # when both strings are empty, it considered interleaving. s1='',s2='',s3=''-> True
                    dp[j]=True
                elif i==0: # when s1 is empty string. s1='',s2='abc',s3='abc'->True
                    dp[j]=dp[j-1] and s2[j]==s3[j]
                elif j==0: # when s2 is empty string. s1='abc',s2='',s3='abc'->True
                    dp[j]=dp[j] and s1[i]==s3[i]
                else:
                    dp[j]=(dp[j] and s1[i]==s3[i+j]) or (dp[j-1] and s2[j]==s3[i+j])
        return dp[-1]
class Solution5:
    # because dp table only accesses the prev row and the prev col, we can have 1d dp
    # memory O(2*len(s2)) time O(m*n)
    def isInterleave(self, s1, s2, s3):
        m,n,l=len(s1),len(s2),len(s3)
        if l!=m+n: return False
        s1,s2,s3='#'+s1,'#'+s2,'#'+s3
        prev=[False]*(n+1)
        for i in range(m+1):
            cur=[False]*(n+1)
            for j in range(n+1):
                if i==0 and j==0: # when both strings are empty, it considered interleaving. s1='',s2='',s3=''-> True
                    cur[j]=True
                elif i==0: # when s1 is empty string. s1='',s2='abc',s3='abc'->True
                    cur[j]=cur[j-1] and s2[j]==s3[j]
                elif j==0: # when s2 is empty string. s1='abc',s2='',s3='abc'->True
                    cur[j]=prev[j] and s1[i]==s3[i]
                else:
                    cur[j]=(prev[j] and s1[i]==s3[i+j]) or (cur[j-1] and s2[j]==s3[i+j])
            prev=cur
        return prev[-1] # or return cur[-1]
class Solution4:
    # memory O(m*n) time O(m*n)
    # https://leetcode.com/problems/interleaving-string/discuss/31879/My-DP-solution-in-C%2B%2B
    def isInterleave(self, s1, s2, s3):
        m,n,l=len(s1),len(s2),len(s3)
        if l!=m+n: return False
        s1,s2,s3='#'+s1,'#'+s2,'#'+s3
        dp=[[False]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 and j==0: # when both strings are empty, it considered interleaving. s1='',s2='',s3=''-> True
                    dp[i][j]=True
                elif i==0: # when s1 is empty string. s1='',s2='abc',s3='abc'->True
                    dp[i][j]=(dp[i][j-1] and s2[j]==s3[i+j])
                    # dp[i][j]=(dp[i][j-1] and s2[j]==s3[j])
                elif j==0: # when s2 is empty string. s1='abc',s2='',s3='abc'->True
                    dp[i][j]=(dp[i-1][j] and s1[i]==s3[i+j])
                    # dp[i][j]=(dp[i-1][j] and s1[i]==s3[i])
                else:
                    dp[i][j]=(dp[i-1][j] and s1[i]==s3[i+j]) or (dp[i][j-1] and s2[j]==s3[i+j])
        return dp[-1][-1]
class Solution:
    # it wants you to try to make s3 from the letters of s1 and s2, but without changing the order that letters appear
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def dp(i, j, k):
            if k==l:
                return True
            res=False
            if i<m and s1[i]==s3[k]:
                res|= dp(i + 1, j, k + 1)
            if j<n and s2[j]==s3[k]:
                res|= dp(i, j + 1, k + 1)
            return res


        m,n,l=len(s1),len(s2),len(s3)
        if m+n!=l: return False
        return dp(0, 0, 0)
class Solution2:
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
class Solution3:
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
    def test01(self):
        self.assertEqual(True,get_sol().isInterleave("aabcc","dbbca","aadbbcbcac"))
    def test02(self):
        self.assertEqual(False,get_sol().isInterleave("","","a"))
    def test03(self):
        self.assertEqual(True,get_sol().isInterleave("cabbcaaacacbac","acabaabacabcca","cacabaabacaabccbabcaaacacbac"))
    def test04(self):
        self.assertEqual(False,get_sol().isInterleave("a","","c"))
    def test05(self):
        self.assertEqual(True,get_sol().isInterleave("a","","a"))
    def test06(self):
        self.assertEqual(False,get_sol().isInterleave("db","b","cbb"))
    def test07(self):
        self.assertEqual(False,get_sol().isInterleave("a", "b", "a"))
    def test08(self):
        self.assertEqual(True,get_sol().isInterleave("", "", ""))
