import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def minCut(self, s: str) -> int:
        def palindrome(s:str): return s==s[::-1]
        @functools.lru_cache(None)
        def dfs(s:str):
            if palindrome(s): return 0
            res=float('inf')
            for i in range(1,len(s)+1):
                first = s[:i]
                if not palindrome(first): continue
                second = s[i:]
                res=min(res,1+dfs(second))
            return res

        return dfs(s)

class Solution2:
    def minCut(self, s: str) -> int:
        def createPalindromeLookupTable(s:str):
            n=len(s)
            look=[[0]*n for _ in range(n)]
            for i in range(n): # one letter word is palindrome
                look[i][i]=1
            for i in range(n-1): # two letter word is palindrome if both are same
                if s[i]==s[i+1]:
                    look[i][i+1]=1
            for i in range(n-3,-1,-1):
                for j in range(i,n):
                    if s[i]==s[j] and look[i+1][j-1]:
                        look[i][j]=1
            self.look=look
        def palindrome(i, j):
            return self.look[i][j]
        @functools.lru_cache(None)
        def dfs(l:int,r:int): # both inclusive
            if palindrome(l,r):
                return 0
            res=float('inf')
            for i in range(l,r):
                if not palindrome(l,i):
                    continue
                res=min(res,1+dfs(i+1,r))
            return res

        createPalindromeLookupTable(s)
        return dfs(0,len(s)-1)

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, get_sol().minCut('aab'))
    def test2(self):
        self.assertEqual(0, get_sol().minCut('aaa'))
    def test3(self):
        self.assertEqual(1, get_sol().minCut("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    def test4(self):
        self.assertEqual(1, get_sol().minCut("abbaaaaa"))
