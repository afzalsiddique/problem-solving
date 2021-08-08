import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix=[words[0]]
        for i in range(1,len(words)):
            prefix.append(prefix[-1]+words[i])

        for x in prefix:
            if x==s: return True
        return False

class Tester(unittest.TestCase):
    def test_1(self):
        s = "iloveleetcode"
        words = ["i","love","leetcode","apples"]
        Output= True
        self.assertEqual(Output,get_sol().isPrefixString(s,words))
    def test_2(self):
        s = "iloveleetcode"
        words = ["apples","i","love","leetcode"]
        Output= False
        self.assertEqual(Output,get_sol().isPrefixString(s,words))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
