import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD=10**9+7
        @functools.lru_cache(None)
        def dfs(i):
            if i==len(s):
                return 1
            if s[i]=='0':
                return 0
            num=0
            res=0
            for j in range(i,len(s)):
                num=num*10+ord(s[j])-ord('0')
                if num>k:
                    break
                res+=dfs(j+1)
                res%=MOD
            return res

        return dfs(0)



class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(1, get_sol().numberOfArrays( s = "1000", k = 10000))
    def test02(self):
        self.assertEqual(0, get_sol().numberOfArrays(s = "1000", k = 10))
    def test03(self):
        self.assertEqual(8, get_sol().numberOfArrays( s = "1317", k = 2000))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
