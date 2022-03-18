from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(i):
            if i==n: return 1
            if s[i]=='0': return 0
            res=0
            res+=dfs(i+1)
            if i<n-1 and int(s[i:i+2])<=26:
                res+=dfs(i+2)
            return res

        n=len(s)
        return dfs(0)
class Solution3:
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
    def test01(self):
        self.assertEqual(2, get_sol().numDecodings('12'))
    def test02(self):
        self.assertEqual(3, get_sol().numDecodings('226'))
    def test03(self):
        self.assertEqual(0, get_sol().numDecodings('0'))
    def test04(self):
        self.assertEqual(0, get_sol().numDecodings('06'))
    def test05(self):
        self.assertEqual(433494437, get_sol().numDecodings('111111111111111111111111111111111111111111'))
    def test06(self):
        self.assertEqual(2, get_sol().numDecodings('11'))
    def test07(self):
        self.assertEqual(1, get_sol().numDecodings( '10'))
    def test08(self):
        self.assertEqual(0, get_sol().numDecodings( '01'))
    def test10(self):
        self.assertEqual(0, get_sol().numDecodings( '0002'))
    def test11(self):
        self.assertEqual(1, get_sol().numDecodings( '27'))
    def test12(self):
        self.assertEqual(1, get_sol().numDecodings( '72'))
    def test13(self):
        self.assertEqual(3, get_sol().numDecodings( '121'))
    def test14(self):
        self.assertEqual(2, get_sol().numDecodings( '811'))
    def test15(self):
        self.assertEqual(2, get_sol().numDecodings( '181'))
    def test16(self):
        self.assertEqual(3, get_sol().numDecodings('118'))
    def test17(self):
        self.assertEqual(3, get_sol().numDecodings('2262'))
    def test18(self):
        self.assertEqual(3, get_sol().numDecodings('226'))
    def test19(self):
        self.assertEqual(0, get_sol().numDecodings('0'))
    def test20(self):
        self.assertEqual(0, get_sol().numDecodings('230'))
    def test21(self):
        self.assertEqual(4, get_sol().numDecodings('227257'))
