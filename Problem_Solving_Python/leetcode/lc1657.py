import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/determine-if-two-strings-are-close/discuss/935920/C%2B%2B-Short-and-Simple-oror-O(-N-)-solution
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)
        li1 = sorted(count1.values())
        li2 = sorted(count2.values())
        return set(word1)==set(word2) and li1==li2
class Solution2:
    # https://leetcode.com/problems/determine-if-two-strings-are-close/discuss/1029064/Python-Oneliner-with-Counter-explained
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)
        cnt1 = Counter(count1.values())
        cnt2 = Counter(count2.values())
        return set(word1)==set(word2) and cnt1 == cnt2

class tester(unittest.TestCase):
    def test_0(self):
        word1 = "abcc"
        word2 = "cbca"
        Output= True
        self.assertEqual(Output,get_sol().closeStrings(word1,word2))
    def test_1(self):
        word1 = "abc"
        word2 = "bca"
        Output= True
        self.assertEqual(Output,get_sol().closeStrings(word1,word2))
    def test_2(self):
        word1 = "a"
        word2 = "aa"
        Output= False
        self.assertEqual(Output,get_sol().closeStrings(word1,word2))
    def test_3(self):
        word1 = "cabbba"
        word2 = "abbccc"
        Output= True
        self.assertEqual(Output,get_sol().closeStrings(word1,word2))
    def test_4(self):
        word1 = "cabbba"
        word2 = "aabbss"
        Output= False
        self.assertEqual(Output,get_sol().closeStrings(word1,word2))
    def test_5(self):
        word1 = "uau"
        word2 = "ssx"
        Output= False
        self.assertEqual(Output,get_sol().closeStrings(word1,word2))
    # def test_6(self):