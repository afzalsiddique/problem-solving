import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1: return ""
        li=list(palindrome)
        for i in range(len(li)//2):
            if li[i]!='a':
                li[i]='a'
                return ''.join(li)
        li[-1]='b'
        return ''.join(li)
class tester(unittest.TestCase):
    def test_1(self):
        palindrome = "abccba"
        Output= "aaccba"
        self.assertEqual(Output,get_sol().breakPalindrome(palindrome))
    def test_2(self):
        palindrome = "a"
        Output= ""
        self.assertEqual(Output,get_sol().breakPalindrome(palindrome))
    def test_3(self):
        palindrome = "aa"
        Output= "ab"
        self.assertEqual(Output,get_sol().breakPalindrome(palindrome))
    def test_4(self):
        palindrome = "aba"
        Output= "abb"
        self.assertEqual(Output,get_sol().breakPalindrome(palindrome))
    def test_5(self):
        palindrome = "aabaa"
        Output= "aabab"
        self.assertEqual(Output,get_sol().breakPalindrome(palindrome))
    def test_6(self):
        palindrome = "aaaabaaaa"
        Output= "aaaabaaab"
        self.assertEqual(Output,get_sol().breakPalindrome(palindrome))
