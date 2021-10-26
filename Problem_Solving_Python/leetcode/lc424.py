import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution2()
######################################################
#  NO_CHARS_REPLACED = WINDOW_SIZE - MOST_FREQ_LETTER
######################################################
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left,right=0,0
        count = Counter()
        maxx=0
        while right<n:
            count[s[right]]+=1
            right+=1
            if right-left-max(count.values())>k:
                count[s[left]]-=1
                left+=1
            maxx = max(maxx, right-left)
        return maxx
class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        count = Counter()
        start,maxx = 0,0
        for end in range(n):
            count[s[end]]+=1
            most_freq_letter_cnt = max(count.values())
            letters_to_change = end-start+1-most_freq_letter_cnt
            if letters_to_change>k:
                count[s[start]]-=1
                start+=1
            maxx = max(maxx, end-start+1)
        return maxx
class Solution3:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        count = Counter()
        start,maxx = 0,0
        for end in range(n):
            count[s[end]]+=1
            while end-start+1-max(count.values())>k:
                count[s[start]]-=1
                start+=1
            maxx = max(maxx, end-start+1)
        return maxx
class Solution4:
    def characterReplacement(self, s: str, k: int) -> int:
        def f(ch): # every char except 'ch' will be replaced
            n=len(s)
            left,right = 0,0
            cnt = 0
            res = 0
            while right<n:
                if cnt>k:
                    cnt-= s[left] != ch
                    left+=1
                while right<n and cnt<=k:
                    cnt+= s[right] != ch
                    right+=1
                    if cnt<=k:
                        res=max(res,right-left)
            return res
        return max(f(letter) for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

class MyTestCase(unittest.TestCase):
    def test1(self):
        expected = 4
        self.assertEqual(expected, get_sol().characterReplacement("ABAB",2))
    def test2(self):
        expected = 4
        self.assertEqual(expected, get_sol().characterReplacement("AABABBA", 1))
    def test3(self):
        expected = 5
        self.assertEqual(expected, get_sol().characterReplacement("AAAAA", 1))
    def test4(self):
        expected = 6
        self.assertEqual(expected, get_sol().characterReplacement("AAAAAB", 1))
    def test5(self):
        expected = 6
        self.assertEqual(expected, get_sol().characterReplacement("BAAAAA", 1))
    def test6(self):
        expected = 4
        self.assertEqual(expected, get_sol().characterReplacement("AABB", 3))
    def test7(self):
        expected = 5
        self.assertEqual(expected, get_sol().characterReplacement("ABCABCAB", 3))
    def test8(self):
        expected = 4
        self.assertEqual(expected, get_sol().characterReplacement("ABCABCAB", 2))
    def test9(self):
        expected = 5
        self.assertEqual(expected, get_sol().characterReplacement("ABCDABCDAB", 3))
