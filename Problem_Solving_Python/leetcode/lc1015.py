import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/smallest-integer-divisible-by-k/discuss/260875/Python-O(K)-with-Detailed-Explanations
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%10 not in {1,3,7,9}: return -1
        mod_set=set()
        num=0
        for length in range(1,k+1):
            num = num*10+1
            mod = num%k
            if not mod: return length
            if mod in mod_set: return -1
            mod_set.add(mod)
        return -1
class tester(unittest.TestCase):
    def test_1(self):
        k = 1
        Output= 1
        self.assertEqual(Output, get_sol().smallestRepunitDivByK(k))
    def test_2(self):
        k = 2
        Output= -1
        self.assertEqual(Output, get_sol().smallestRepunitDivByK(k))
    def test_3(self):
        k = 3
        Output= 3
        self.assertEqual(Output, get_sol().smallestRepunitDivByK(k))
    def test_4(self):
        k = 197
        Output= 98
        self.assertEqual(Output, get_sol().smallestRepunitDivByK(k))
    def test_5(self):
        k = 19927
        Output= 19926
        self.assertEqual(Output, get_sol().smallestRepunitDivByK(k))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):