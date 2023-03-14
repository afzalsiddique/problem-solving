import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # checkout the image 'lc940img.jpg' in the same folder or https://ibb.co/D9svNYM
    def distinctSubseqII(self, s: str) -> int:
        MOD=10**9+7
        dp=[0]*26 # no of subsequences ending with a specific char
        for c in s:
            idx=ord(c)-ord('a')
            dp[idx]=sum(dp)+1 # add this letter to the end of all previously found subsequences
            dp[idx]%=MOD
        return sum(dp)%MOD
class Solution2:
    def distinctSubseqII(self, s: str) -> int:
        M=10**9+7
        s='#'+s
        n=len(s)
        dp=[[0]*26 for _ in range(n)]
        for i in range(1,n):
            tmp=sum(dp[i-1][j] for j in range(26))%M
            for j in range(26):
                dp[i][j]=dp[i-1][j]
            dp[i][ord(s[i])-ord('a')]=(tmp+1)%M
        return sum(dp[-1][j] for j in range(26))%M
class Solution3:
    # recursive
    def distinctSubseqII(self, s: str) -> int:
        MOD=10**9+7
        def f(i):
            idx = ord(s[i])-ord('a')
            if i==0:
                dp=[0]*26
                dp[idx]=1
                return dp
            dp=f(i-1)
            dp[idx]=sum(dp)+1 # add this letter to the end of all previously found subsequences
            dp[idx]%=MOD
            return dp

        dp=f(len(s)-1)
        return sum(dp)%MOD


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(7, get_sol().distinctSubseqII("abc"))
    def test02(self):
        self.assertEqual(6, get_sol().distinctSubseqII("aba"))
    def test03(self):
        self.assertEqual(3, get_sol().distinctSubseqII("aaa"))
    def test04(self):
        self.assertEqual(20, get_sol().distinctSubseqII("aaabba")) # checkout the image 'lc940img.jpg' in the same folder or https://ibb.co/D9svNYM
    def test05(self):
        self.assertEqual(97915677, get_sol().distinctSubseqII("zchmliaqdgvwncfatcfivphddpzjkgyygueikthqzyeeiebczqbqhdytkoawkehkbizdmcnilcjjlpoeoqqoqpswtqdpvszfaksn"))
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):
