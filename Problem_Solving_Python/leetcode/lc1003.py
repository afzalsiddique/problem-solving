import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        i=len(s)-1
        while True:
            if len(st)>i+1: return False
            if s[i]!='c' and not st: return False
            while st and st[-1]==s[i]:
                st.pop()
                i-=1
            if i==-1:
                if not st: return True
                return False
            if s[i]=='c':
                st.extend('abc')
            else:
                return False
class tester(unittest.TestCase):
    def test_1(self):
        s = "aabcbc"
        Output= True
        self.assertEqual(Output,get_sol().isValid(s))
    def test_2(self):
        s = "abcabcababcc"
        Output= True
        self.assertEqual(Output,get_sol().isValid(s))
    def test_3(self):
        s = "abccba"
        Output= False
        self.assertEqual(Output,get_sol().isValid(s))
    def test_4(self):
        s = "cababc"
        Output= False
        self.assertEqual(Output,get_sol().isValid(s))
    def test_5(self):
        s = "bac"
        Output= False
        self.assertEqual(Output,get_sol().isValid(s))
    # def test_6(self):
    # def test_7(self):