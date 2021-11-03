import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def mask(s:str): # 'hello' -> 'h*ll*'
            return ''.join('*' if c in 'aeiou' else c for c in s)

        res = []
        sett = set(wordlist)
        lower = {}
        vowel = {}
        for w in wordlist[::-1]:
            lo = w.lower()
            vow = mask(w.lower()) # lower and put mask
            lower[lo]=w
            vowel[vow]=w

        for q in queries:
            lo = q.lower()
            vow = mask(q.lower()) # lower and put mask
            if q in sett:
                res.append(q)
            elif lo in lower:
                res.append(lower[lo])
            elif vow in vowel:
                res.append(vowel[vow])
            else:
                res.append("")
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        wordlist,queries = ["KiTe","kite","hare","Hare"],  ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
        Output= ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
        self.assertEqual(Output, get_sol().spellchecker(wordlist, queries))
    def test2(self):
        wordlist,queries = ["yellow"],  ["YellOw"]
        Output= ["yellow"]
        self.assertEqual(Output, get_sol().spellchecker(wordlist, queries))
    def test3(self):
        wordlist,queries = ["ae","aa"], ["UU"]
        Output= ["ae"]
        self.assertEqual(Output, get_sol().spellchecker(wordlist, queries))
    # def test4(self):
    # def test5(self):
