import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # time O(sqrt(n)) space O(1)
    def kthFactor(self, n: int, k: int) -> int:
        k-=1 # zero based

        d=1
        while d*d<=n:
            if n%d==0:
                if not k:
                    return d
                k-=1
            d+=1

        d-=1
        if d*d==n:
            d-=1

        while d>=1:
            if n%d==0:
                if not k:
                    return n//d
                k-=1
            d-=1
        return -1
class Solution2:
    # bad solution
    # time O(sqrt(n)) space O(sqrt(n))
    def kthFactor(self, n: int, k: int) -> int:
        li1 = []
        li2 = []
        i=1
        while i*i<=n:
            if n%i==0:
                if i*i==n:
                    li1.append(i)
                else:
                    li1.append(i)
                    li2.append(n//i)
            i+=1
        li = li1 + list(reversed(li2))
        if len(li)<k: return -1
        return li[k-1]
class MyTestCase(unittest.TestCase):
    def test1(self):
        n,k = 12,  3
        Output= 3
        self.assertEqual(Output, get_sol().kthFactor(n,k))
    def test2(self):
        n,k = 7,  2
        Output= 7
        self.assertEqual(Output, get_sol().kthFactor(n,k))
    def test3(self):
        n,k = 4,  4
        Output= -1
        self.assertEqual(Output, get_sol().kthFactor(n,k))
    def test4(self):
        n,k = 1,  1
        Output= 1
        self.assertEqual(Output, get_sol().kthFactor(n,k))
    def test5(self):
        n,k = 1000,  3
        Output= 4
        self.assertEqual(Output, get_sol().kthFactor(n,k))
