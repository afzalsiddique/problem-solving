import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        cnt=0
        for i in range(n-2):
            tmp = s[i:i+3]
            if len(set(tmp))==len(tmp):
                cnt+=1
        return cnt

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