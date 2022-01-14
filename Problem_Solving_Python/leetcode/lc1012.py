import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # tle
    def numDupDigitsAtMostN(self, n: int) -> int:
        def dfs(s:str):
            nonlocal res
            if len(set(s))!=len(s):
                return
            if int(s)>n or int(s)<1:
                return
            res+=1
            for i in range(9+1):
                dfs(s+str(i))


        res=0
        for i in range(1,9+1):
            dfs(str(i))
        return n-res

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(1,get_sol().numDupDigitsAtMostN(20))
    def test02(self):
        self.assertEqual(10,get_sol().numDupDigitsAtMostN(100))
    def test03(self):
        self.assertEqual(262,get_sol().numDupDigitsAtMostN(1000))
    def test04(self):
        self.assertEqual(612924,get_sol().numDupDigitsAtMostN(743610))
    def test05(self):
        self.assertEqual(612924,get_sol().numDupDigitsAtMostN(1000000000))
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
