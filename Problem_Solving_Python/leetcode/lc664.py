import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def strangePrinter(self, s: str) -> int:
        @functools.lru_cache(None)
        def func(i,j,k):
            if i>j: return 0
            if i==j: return 1
            res=float('inf')
            if s[i]==s[i+1]:
                res=min(res,1+func(i+1,j,k+1))
            for m in range(i+1,j+1):
                if s[i]==s[m]:
                    part1=func(i+1,m-1,0)
                    part2=func(m,j,k+1)
                    res=min(res,part1+part2)
                else:
                    part1=1
                    part2=func(i+1,j,0)
                    res=min(res,part1+part2)
            return res

        return func(0,len(s)-1,0)



class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, get_sol().strangePrinter("abbb"))
    def test2(self):
        self.assertEqual(2, get_sol().strangePrinter("aaabbb"))
    def test3(self):
        self.assertEqual(2, get_sol().strangePrinter("aba"))
    def test4(self):
        self.assertEqual(1, get_sol().strangePrinter("bb"))
    def test5(self):
        self.assertEqual(1, get_sol().strangePrinter("bbb"))
    def test6(self):
        self.assertEqual(1, get_sol().strangePrinter("bbb"))
    def test7(self):
        self.assertEqual(14, get_sol().strangePrinter("abcdefghijklmn"))

