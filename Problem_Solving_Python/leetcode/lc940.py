import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # no of subsequences ending with a specific char
    def distinctSubseqII(self, s: str) -> int:
        MOD=10**9+7
        dp=[0]*26
        for c in s:
            idx=ord(c)-ord('a')
            tmp=sum(x for x in dp)
            dp[idx]=tmp+1
            dp[idx]%=MOD
        return sum(dp)%MOD



class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(7, get_sol().distinctSubseqII("abc"))
    def test2(self):
        self.assertEqual(6, get_sol().distinctSubseqII("aba"))
    def test3(self):
        self.assertEqual(3, get_sol().distinctSubseqII("aaa"))
    def test4(self):
        self.assertEqual(97915677, get_sol().distinctSubseqII("zchmliaqdgvwncfatcfivphddpzjkgyygueikthqzyeeiebczqbqhdytkoawkehkbizdmcnilcjjlpoeoqqoqpswtqdpvszfaksn"))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):
