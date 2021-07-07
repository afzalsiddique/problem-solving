import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res=[]
        def f(n,k):
            if n==0: return
            if k-1<=26*(n-1):
                res.append('a')
                k-=1
            else:
                tmp = k%26
                if tmp==0: tmp=26
                res.append(chr(ord('a')+tmp-1))
                k-=tmp
            n-=1
            f(n,k)
        f(n,k)
        return ''.join(res)
class tester(unittest.TestCase):
    def test_1(self):
        n = 3
        k = 27
        Output= "aay"
        self.assertEqual(Output,get_sol().getSmallestString(n,k))
    def test_2(self):
        n = 2
        k = 28
        Output= "bz"
        self.assertEqual(Output,get_sol().getSmallestString(n,k))
    def test_3(self):
        n = 2
        k = 27
        Output= "az"
        self.assertEqual(Output,get_sol().getSmallestString(n,k))
    def test_4(self):
        n = 5
        k = 73
        Output= "aaszz"
        self.assertEqual(Output,get_sol().getSmallestString(n,k))
    # def test_5(self):
    # def test_6(self):
