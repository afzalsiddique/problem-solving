import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b in a: return 1
        if b in (a+a): return 2
        index = b.find(a)
        res=1
        if index !=0: # check left of 'index'
            j=index-1
            i=len(a)-1
            while j!=-1:
                if a[i]!=b[j]: return -1
                j-=1
                i-=1
            res+=1

        j = index+len(a)
        while j<len(b):
            i=0
            res+=1
            while i<len(a) and j<len(b):
                if a[i]!=b[j]: return -1
                i+=1
                j+=1
        return res



class MyTestCase(unittest.TestCase):
    def test1(self):
        a,b = "abcd",  "cdabcdab"
        Output= 3
        self.assertEqual(Output, get_sol().repeatedStringMatch(a,b))
    def test2(self):
        a,b = "a",  "aa"
        Output= 2
        self.assertEqual(Output, get_sol().repeatedStringMatch(a,b))
    def test3(self):
        a,b = "a",  "a"
        Output= 1
        self.assertEqual(Output, get_sol().repeatedStringMatch(a,b))
    def test4(self):
        a,b = "abc",  "wxyz"
        Output= -1
        self.assertEqual(Output, get_sol().repeatedStringMatch(a,b))
    def test5(self):
        a,b = "aa", "a"
        Output= 1
        self.assertEqual(Output, get_sol().repeatedStringMatch(a,b))
    def test6(self):
        a,b = "aaaaaaaaaaaaaaaaaaaaaab", "ba"
        Output= 2
        self.assertEqual(Output, get_sol().repeatedStringMatch(a,b))