from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        def isPali(s:str): return s==s[::-1]
        @cache
        def dp(i,k): # i: index, k: no of partitions left
            if k==0:
                tmp=s[i:]
                # return len(tmp) and isPali(tmp) # len(tmp) -> non empty partitions
                return isPali(tmp)
            for j in range(i+1,n):
                if isPali(s[i:j]) and dp(j,k-1):
                    return True
            return False

        n=len(s)
        return dp(0,2)

class Solution3:
    def checkPartitioning(self, s: str) -> bool:
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
        @cache
        def dfs(l:int,r:int,k:int):
            if k==1:
                ans= palindrome(l, r)
                return ans
            for i in range(l+1,r+1):
                if not palindrome(l, i - 1):
                    continue
                ans=dfs(i,r,k-1)
                if ans:
                    return True
            return False

        createPalindromeLookupTable(s)
        return dfs(0,len(s)-1,3)
class Solution2:
    def checkPartitioning(self, s: str) -> bool:
        def palindrome(s:str): return s==s[::-1]
        @cache
        def dfs(s:str,k:int):
            if k==1:
                return palindrome(s)
            for i in range(1,len(s)):
                first=s[:i]
                if not palindrome(first): continue
                second=s[i:]
                if dfs(second,k-1): return True
            return False

        return dfs(s,3)


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(True,get_sol().checkPartitioning("abcbdd"))
    def test02(self):
        self.assertEqual(False,get_sol().checkPartitioning("bcbddxy"))
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
