import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n=len(s)
        first_char = ord(s[0])-ord('a')
        left = [0]*26 # prefix sum left
        left[first_char]+=1
        right = [0]*26 # prefix sum right
        for i in range(2,n):
            c = ord(s[i]) - ord('a')
            right[c]+=1

        sett = set()
        for i in range(1,n-1):
            cur_char = ord(s[i]) - ord('a')
            next_char = ord(s[i+1]) - ord('a')
            for j in range(26):
                if left[j] and right[j]:
                    sett.add((j,cur_char,j))
            left[cur_char]+=1
            right[next_char]-=1
        return len(sett)


class MyTestCase(unittest.TestCase):
    def test1(self):
        s = "aabca"
        Output= 3
        self.assertEqual(Output, get_sol().countPalindromicSubsequence(s))
    def test2(self):
        s = "adc"
        Output= 0
        self.assertEqual(Output, get_sol().countPalindromicSubsequence(s))
    def test3(self):
        s = "bbcbaba"
        Output= 4
        self.assertEqual(Output, get_sol().countPalindromicSubsequence(s))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
