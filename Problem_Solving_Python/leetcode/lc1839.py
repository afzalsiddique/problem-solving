import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        di={'a':'ae','e':'ei','i':'io','o':'ou','u':'u'}
        n=len(word)
        maxx=0
        left,right=0,0
        while left<n:
            # l,r=word[left],word[right]
            if word[left]=='a' and word[right]=='u':
                maxx=max(maxx,right-left+1)
            if right+1<n and word[right+1] in di[word[right]]:
                right+=1
            else:
                left=right+1
                right+=1
        return maxx

class MyTestCase(unittest.TestCase):
    def test_1(self):
        word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
        Output= 13
        self.assertEqual(Output, get_sol().longestBeautifulSubstring(word))
    def test_2(self):
        word = "aeeeiiiioooauuuaeiou"
        Output= 5
        self.assertEqual(Output, get_sol().longestBeautifulSubstring(word))
    def test_3(self):
        word = "a"
        Output= 0
        self.assertEqual(Output, get_sol().longestBeautifulSubstring(word))
    def test_4(self):
        word = "aeioauuuaeiou"
        Output= 5
        self.assertEqual(Output, get_sol().longestBeautifulSubstring(word))
    def test_5(self):
        word = "uuuuu"
        Output= 0
        self.assertEqual(Output, get_sol().longestBeautifulSubstring(word))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
