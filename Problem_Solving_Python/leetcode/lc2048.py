import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def valid(num):
            num = str(num)
            count=Counter(num)
            for digit in count:
                if int(digit)!=count[digit]:
                    return False
            return True

        for i in range(n+1,10**9+1):
            if valid(i): return i

class MyTestCase(unittest.TestCase):
    def test1(self):
        n = 1
        Output= 22
        self.assertEqual(Output, get_sol().nextBeautifulNumber(n))
    def test2(self):
        n = 1000
        Output= 1333
        self.assertEqual(Output, get_sol().nextBeautifulNumber(n))
    def test3(self):
        n = 3000
        Output= 3133
        self.assertEqual(Output, get_sol().nextBeautifulNumber(n))
    def test4(self):
        n=59866
        Output = 122333
        self.assertEqual(Output, get_sol().nextBeautifulNumber(n))
    def test5(self):
        n=0
        Output = 1
        self.assertEqual(Output, get_sol().nextBeautifulNumber(n))
    def test6(self):
        n=1000000
        Output = 1224444
        self.assertEqual(Output, get_sol().nextBeautifulNumber(n))
