import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def convert(a):
            return str(ord(a)-97)
        li1=[]
        for a in firstWord:
            li1.append(convert(a))
        li2=[]
        for a in secondWord:
            li2.append(convert(a))
        li3 = []
        for a in targetWord:
            li3.append(convert(a))
        a,b,c=''.join(li1),''.join(li2),''.join(li3)
        if int(a)+int(b)==int(c): return True
        return False


class tester(unittest.TestCase):
    def test1(self):
        s = "bab"
        t = "aba"
        Output= 1
        self.assertEqual(Output,get_sol().minSteps(s,t))
    def test2(self):
        s = "leetcode"
        t = "practice"
        Output= 5
        self.assertEqual(Output,get_sol().minSteps(s,t))
    def test3(self):
        s = "anagram"
        t = "mangaar"
        Output= 0
        self.assertEqual(Output,get_sol().minSteps(s,t))
    def test4(self):
        s = "xxyyzz"
        t = "xxyyzz"
        Output= 0
        self.assertEqual(Output,get_sol().minSteps(s,t))
    def test5(self):
        s = "friend"
        t = "family"
        Output= 4
        self.assertEqual(Output,get_sol().minSteps(s,t))