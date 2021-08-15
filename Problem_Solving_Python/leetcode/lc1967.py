import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cnt=0
        for p in patterns:
            if p in word:
                cnt+=1
        return cnt

# class Tester(unittest.TestCase):
    # def test_1(self):
    #     s = "iloveleetcode"
    #     words = ["i","love","leetcode","apples"]
    #     Output= True
    #     self.assertEqual(Output,get_sol().isPrefixString(s,words))
    # def test_2(self):
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
