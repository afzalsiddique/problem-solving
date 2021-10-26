import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        n=len(s)
        i=0
        li = []
        while i<n:
            j=i
            while j<n and '0'<=s[j]<='9':
                j+=1
            if s[i:j]:
                li.append(int(s[i:j]))
            i=j
            while i<n and ('a'<=s[i]<='z' or s[i]==' '):
                i+=1

        for i in range(len(li)-1):
            if li[i]>=li[i+1]:
                return False
        return True


class MyTestCase(unittest.TestCase):
    def test1(self):
        s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
        Output= True
        self.assertEqual(Output, get_sol().areNumbersAscending(s))
    def test2(self):
        s = "hello world 5 x 5"
        Output= False
        self.assertEqual(Output, get_sol().areNumbersAscending(s))
    def test3(self):
        s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
        Output= False
        self.assertEqual(Output, get_sol().areNumbersAscending(s))
    def test4(self):
        s = "4"
        Output= True
        self.assertEqual(Output, get_sol().areNumbersAscending(s))
    # def test5(self):
    # def test6(self):
