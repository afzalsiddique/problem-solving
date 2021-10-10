import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        def flip(cur_state,i): return cur_state ^ (1<<i)
        no_of_letters = 10
        state = 0
        count = Counter()
        count[state]+=1
        res = 0
        for c in word:
            c = ord(c)-ord('a')
            state = flip(state,c)
            res += count[state]
            count[state]+=1
            for i in range(no_of_letters):
                tmp = flip(state,i)
                res += count[tmp]
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        word = "aba"
        Output= 4
        self.assertEqual(Output, get_sol().wonderfulSubstrings(word))
    def test2(self):
        word = "aabb"
        Output= 9
        self.assertEqual(Output, get_sol().wonderfulSubstrings(word))
    def test3(self):
        word = "he"
        Output= 2
        self.assertEqual(Output, get_sol().wonderfulSubstrings(word))
    def test4(self):
        word = "acbbbb"
        Output= 14
        self.assertEqual(Output, get_sol().wonderfulSubstrings(word))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
