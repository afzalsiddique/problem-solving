import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count=Counter(s)
        tmp= count[s[0]]
        for ch in count:
            if count[ch]!=tmp: return False
        return True
class tester(unittest.TestCase):
    def test_1(self):
        s = "abacbc"
        Output= True
        self.assertEqual(Output, get_sol().areOccurrencesEqual(s))
    def test_2(self):
        s = "aaabb"
        Output= False
        self.assertEqual(Output, get_sol().areOccurrencesEqual(s))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
