import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution2()
class Solution:
    #  NO_CHARS_REPLACED = WINDOW_SIZE - MOST_FREQ_LETTER
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
class Solution4:
    # sliding window template
    def characterReplacement(self, s: str, k: int) -> int:
        def replace(char:str):
            left,right=0,0
            res=0
            operationLeft=k
            while right<len(s):
                while right<len(s):
                    if not operationLeft and s[right]!=char:
                        break
                    if s[right]!=char:
                        operationLeft-=1
                    right+=1
                res=max(res,right-left)
                if left<len(s) and s[left]!=char:
                    operationLeft+=1
                left+=1
            return res

        res=0
        for char in string.ascii_uppercase:
            res=max(res,replace(char))
        return res
class Solution2:
    #  NO_CHARS_REPLACED = WINDOW_SIZE - MOST_FREQ_LETTER
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
    #  NO_CHARS_REPLACED = WINDOW_SIZE - MOST_FREQ_LETTER
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
class Solution5:
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
    def test01(self):
        self.assertEqual(4, get_sol().characterReplacement("ABAB",2))
    def test02(self):
        self.assertEqual(4, get_sol().characterReplacement("AABABBA", 1))
    def test03(self):
        self.assertEqual(5, get_sol().characterReplacement("AAAAA", 1))
    def test04(self):
        self.assertEqual(6, get_sol().characterReplacement("AAAAAB", 1))
    def test05(self):
        self.assertEqual(6, get_sol().characterReplacement("BAAAAA", 1))
    def test06(self):
        self.assertEqual(4, get_sol().characterReplacement("AABB", 3))
    def test07(self):
        self.assertEqual(5, get_sol().characterReplacement("ABCABCAB", 3))
    def test08(self):
        self.assertEqual(4, get_sol().characterReplacement("ABCABCAB", 2))
    def test09(self):
        self.assertEqual(5, get_sol().characterReplacement("ABCDABCDAB", 3))
    def test10(self):
        self.assertEqual(4, get_sol().characterReplacement("AAAA", 0))
