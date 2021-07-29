import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/construct-k-palindrome-strings/discuss/563379/JavaC%2B%2BPython-Straight-Forward
    def canConstruct(self, s: str, k: int) -> bool:
        n=len(s)
        count = Counter(s)
        odd_counts=0
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if count[c]%2: odd_counts+=1
        return odd_counts<=k and k<=n
class tester(unittest.TestCase):
    def test_1(self):
        s,k= "annabelle",2
        Output= True
        self.assertEqual(Output,get_sol().canConstruct(s,k))
    def test_2(self):
        s,k= "leetcode",3
        Output= False
        self.assertEqual(Output,get_sol().canConstruct(s,k))
    def test_3(self):
        s,k= "true",4
        Output= True
        self.assertEqual(Output,get_sol().canConstruct(s,k))
    def test_4(self):
        s,k= "yzyzyzyzyzyzyzy",2
        Output= True
        self.assertEqual(Output,get_sol().canConstruct(s,k))
    def test_5(self):
        s,k= "cr",7
        Output= False
        self.assertEqual(Output,get_sol().canConstruct(s,k))
    def test_6(self):
        s,k= "annabelle", 2
        Output= True
        self.assertEqual(Output,get_sol().canConstruct(s,k))
    def test_7(self):
        s,k= "messi", 3
        Output= True
        self.assertEqual(Output,get_sol().canConstruct(s,k))
    # def test_8(self):