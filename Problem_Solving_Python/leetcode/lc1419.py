import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        def get_max():
            maxx=0
            for ch in 'croak': maxx=max(maxx,count[ch])
            return maxx
        count=Counter()
        count['#']=float('inf')
        prev={'c':'#','r':'c','o':'r','a':'o','k':'a'}
        maxx=float('-inf')
        for ch in croakOfFrogs:
            count[ch]+=1
            if count[ch]>count[prev[ch]]: return -1
            maxx=max(maxx,get_max())
            if ch=='k':
                for ch2 in 'croak':
                    count[ch2]-=1
        for ch in 'croak':
            if count[ch]!=0: return -1
        return maxx

class Tester(unittest.TestCase):
    def test_1(self):
        croakOfFrogs = "croakcroak"
        Output= 1
        self.assertEqual(Output,get_sol().minNumberOfFrogs(croakOfFrogs))
    def test_2(self):
        croakOfFrogs = "crcoakroak"
        Output= 2
        self.assertEqual(Output,get_sol().minNumberOfFrogs(croakOfFrogs))
    def test_3(self):
        croakOfFrogs = "croakcrook"
        Output= -1
        self.assertEqual(Output,get_sol().minNumberOfFrogs(croakOfFrogs))
    def test_4(self):
        croakOfFrogs = "croakcroa"
        Output= -1
        self.assertEqual(Output,get_sol().minNumberOfFrogs(croakOfFrogs))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
