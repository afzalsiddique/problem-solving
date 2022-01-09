import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # print(Counter(words))
        di=Counter()
        res=0
        for word in words:
            rev=word[::-1]
            if di[rev]>0:
                di[rev]-=1
                res+=4
                continue
            di[word]+=1
        for word in di:
            if di[word] and word[0]==word[1]:
                res+=2
                break
        return res

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(6, get_sol().longestPalindrome(["lc","cl","gg"]))
    def test_2(self):
        self.assertEqual(8, get_sol().longestPalindrome(["ab","ty","yt","lc","cl","ab"]))
    def test_3(self):
        self.assertEqual(2, get_sol().longestPalindrome(["cc","ll","xx"]))
    def test_4(self):
        self.assertEqual(22, get_sol().longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]))
    def test_5(self):
        self.assertEqual(14, get_sol().longestPalindrome(["em","pe","mp","ee","pp","me","ep","em","em","me"]))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
