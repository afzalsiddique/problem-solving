import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def h(start:int):
            if start==n:
                self.maxx=max(self.maxx,len(sett))
                return
            for i in range(start+1,n+1):
                first=s[start:i]
                if first in sett: continue
                sett.add(first)
                h(i)
                sett.remove(first)

        n=len(s)
        sett=set()
        self.maxx=0
        h(0)
        return self.maxx
class Solution2:
    def maxUniqueSplit(self, s: str) -> int:
        def h(s):
            if not s:
                self.maxx=max(self.maxx,len(sett))
                return
            for i in range(1,len(s)+1):
                first=s[:i]
                second=s[i:]
                if first in sett: continue
                sett.add(first)
                h(second)
                sett.remove(first)

        sett=set()
        self.maxx=0
        h(s)
        return self.maxx
class MyTestCase(unittest.TestCase):
    def test_1(self):
        s = "ababccc"
        Output= 5
        self.assertEqual(Output, get_sol().maxUniqueSplit(s))
    def test_2(self):
        s = "aba"
        Output= 2
        self.assertEqual(Output, get_sol().maxUniqueSplit(s))
    def test_3(self):
        s = "aa"
        Output= 1
        self.assertEqual(Output, get_sol().maxUniqueSplit(s))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):