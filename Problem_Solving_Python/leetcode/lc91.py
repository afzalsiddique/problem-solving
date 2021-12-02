import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
def get_sol(): return Solution()
class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(s:str):
            if s in dp: return dp[s]
            if not s: return 1
            if s[0]=='0': return 0
            if len(s)==1: return 1
            ans=0
            ans+=dfs(s[1:])
            two_digits=s[:2]
            if int(two_digits)<=26:
                ans+=dfs(s[2:])
            dp[s]=ans
            return ans

        dp={}
        return dfs(s)
class Solution3:
    def numDecodings(self, s: str) -> int:
        @functools.lru_cache(None)
        def dfs(s:str):
            if not s: return 1
            if s[0]=='0': return 0
            if len(s)==1: return 1
            return dfs(s[1:]) + (dfs(s[2:]) if int(s[:2])<=26 else 0)

        return dfs(s)
class Solution2:
    def numDecodings(self, s: str) -> int:
        di = {}
        def decode(s:str):
            n = len(s)
            if n==0:return 1
            if n==1:
                return 1 if s!='0' else 0
            if s in di:return di[s]
            ans = 0
            first,second = s[0],s[1]
            # considering one char
            if first!='0':
                ans+=decode(s[1:])
            # considering two chars
            if first=='1':
                ans+=decode(s[2:])
            elif first=='2' and second>='0' and second<='6':
                ans += decode(s[2:])
            di[s]=ans
            return di[s]

        return decode(s)


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, Solution().numDecodings('12'))
    def test2(self):
        self.assertEqual(3, Solution().numDecodings('226'))
    def test3(self):
        self.assertEqual(0, Solution().numDecodings('0'))
    def test4(self):
        self.assertEqual(0, Solution().numDecodings('06'))
    def test5(self):
        self.assertEqual(433494437, Solution().numDecodings('111111111111111111111111111111111111111111'))
    def test_1(self):
        self.assertEqual(2, get_sol().numDecodings(s = '11'))
    def test_2(self):
        self.assertEqual(1, get_sol().numDecodings(s = '10'))
    def test_3(self):
        self.assertEqual(0, get_sol().numDecodings(s = '01'))
    def test_4(self):
        self.assertEqual(0, get_sol().numDecodings(s = '0002'))
    def test_5(self):
        self.assertEqual(1, get_sol().numDecodings(s = '27'))
    def test_6(self):
        self.assertEqual(1, get_sol().numDecodings(s = '72'))
    def test_7(self):
        self.assertEqual(3, get_sol().numDecodings(s = '121'))
    def test_8(self):
        self.assertEqual(2, get_sol().numDecodings(s = '811'))
    def test_9(self):
        self.assertEqual(2, get_sol().numDecodings(s = '181'))
    def test_10(self):
        self.assertEqual(3, get_sol().numDecodings(s = '118'))
    def test_11(self):
        self.assertEqual(3, get_sol().numDecodings(s = '2262'))
    def test_12(self):
        self.assertEqual(3, get_sol().numDecodings(s = '226'))
    def test_13(self):
        self.assertEqual(0, get_sol().numDecodings(s = '0'))
    def test_14(self):
        self.assertEqual(0, get_sol().numDecodings(s = '230'))
    def test_15(self):
        self.assertEqual(4, get_sol().numDecodings(s = '227257'))
