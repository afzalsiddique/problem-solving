import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minimumLength(self, s: str) -> int:
        def remove(li:deque):
            n=len(li)
            if n==1: return False
            if n==0: return False
            first=li[0]
            last=li[-1]
            if first!=last: return False
            while li and li[0]==first:
                li.popleft()
            while li and li[-1]==last:
                li.pop()
            return True

        li=deque(s)
        while remove(li):
            pass
        return len(li)



class MyTestCase(unittest.TestCase):
    def test_1(self):
        s = "ca"
        Output= 2
        self.assertEqual(Output, get_sol().minimumLength(s))
    def test_2(self):
        s = "cabaabac"
        Output= 0
        self.assertEqual(Output, get_sol().minimumLength(s))
    def test_3(self):
        s = "aabccabba"
        Output= 3
        self.assertEqual(Output, get_sol().minimumLength(s))
    def test_4(self):
        s="bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"
        Output = 1
        self.assertEqual(Output, get_sol().minimumLength(s))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):