import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set('aeiou')
        cnt=0
        for i in range(k-1):
            if s[i] in vowels:
                cnt+=1
        # print(len(s))
        maxx=0
        for i in range(k-1,len(s)):
            if s[i] in vowels:
                cnt+=1
            maxx=max(maxx,cnt)
            if s[i-k+1] in vowels:
                cnt-=1
        return maxx

class tester(unittest.TestCase):
    def test_1(self):
        s = "abciiidef"
        k = 3
        Output= 3
        self.assertEqual(Output,get_sol().maxVowels(s,k))
    def test_2(self):
        s = "aeiou"
        k = 2
        Output= 2
        self.assertEqual(Output,get_sol().maxVowels(s,k))
    def test_3(self):
        s = "leetcode"
        k = 3
        Output= 2
        self.assertEqual(Output,get_sol().maxVowels(s,k))
    def test_4(self):
        s = "rhythms"
        k = 4
        Output= 0
        self.assertEqual(Output,get_sol().maxVowels(s,k))
    def test_5(self):
        s = "tryhard"
        k = 4
        Output= 1
        self.assertEqual(Output,get_sol().maxVowels(s,k))
    def test_6(self):
        s = "qempburycnhrvvccr"
        k = 13
        Output= 2
        self.assertEqual(Output,get_sol().maxVowels(s,k))
    # def test_7(self):