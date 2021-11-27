import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    def countVowels(self, s: str) -> int:
        n=len(s)
        res=0
        for i in range(n):
            if s[i] in 'aeiou':
                res+=(i+1)*(n-i)
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        word = "aba"
        Output= 6
        self.assertEqual(Output, get_sol().countVowels(word))
    def test2(self):
        word = "abc"
        Output= 3
        self.assertEqual(Output, get_sol().countVowels(word))
    def test3(self):
        word = "ltcd"
        Output= 0
        self.assertEqual(Output, get_sol().countVowels(word))
    def test4(self):
        word = "noosabasboosa"
        Output= 237
        self.assertEqual(Output, get_sol().countVowels(word))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
