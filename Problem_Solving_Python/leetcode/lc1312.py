from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *
def get_sol(): return Solution()
# https://www.youtube.com/watch?v=DOnK40BvazI&t=300s
################# SAME AS LONGEST COMMON SUBSEQUENCE ##########
################ SAME AS LONGEST PALINDROMIC SUBSEQUENCE ###########
class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def dp(i,j):
            if i>=j: return 0
            if s[i]==s[j]: return dp(i+1,j-1)
            return 1+min(dp(i+1,j),dp(i,j-1))

        return dp(0,len(s)-1)
class Solution2:
    def minInsertions(self, s: str) -> int:
        di = {}
        def helper(s):
            n = len(s)
            if n==0 or n==1:return 0
            if n==2:
                if s[0]==s[1]:return 0
                else: return 1
            if s in di:return di[s]
            if s[0]==s[-1]:
                di[s] = helper(s[1:-1]) # remove one char from both ends
                return di[s]
            else:
                di[s]= 1+min(helper(s[:-1]), helper(s[1:]))
                return di[s]

        return helper(s)
class Solution3:
    # longest common subsequecne
    def minInsertions2(self, s: str) -> int:
        n = len(s)
        s2 = s[::-1]
        dp = [[-1]*n for _ in range(n)]

        def helper(m,n):#longest common subsequence
            if m==-1 or n==-1:return 0
            if dp[m][n]!=-1:return dp[m][n]
            if s[m]==s2[n]:
                dp[m][n] = 1 + helper(m-1,n-1)
            else:
                dp[m][n] = max(helper(m-1,n),helper(m,n-1))
            return dp[m][n]


        return n - helper(n-1,n-1)




class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(0, get_sol().minInsertions('zzazz'))
    def test02(self):
        self.assertEqual(2, get_sol().minInsertions( "mbadm" ))
    def test03(self):
        self.assertEqual(5, get_sol().minInsertions( "leetcode" ))
    def test04(self):
        self.assertEqual(5, get_sol().minInsertions( "zjveiiwvc" ))
