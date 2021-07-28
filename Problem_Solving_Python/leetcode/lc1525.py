import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    def numSplits(self, s: str) -> int:
        count1=Counter(s)
        count2=Counter()
        res=0
        for x in s:
            count2[x]+=1
            count1[x]-=1
            if count1[x]==0:
                count1.pop(x)
            if len(count1)==len(count2):
                res+=1
        return res

class tester(unittest.TestCase):
    def test_1(self):
        s = "aacaba"
        Output= 2
        self.assertEqual(Output,get_sol().numSplits(s))
    def test_2(self):
        s = "abcd"
        Output= 1
        self.assertEqual(Output,get_sol().numSplits(s))
    def test_3(self):
        s = "aaaaa"
        Output= 4
        self.assertEqual(Output,get_sol().numSplits(s))
    def test_4(self):
        s = "acbadbaada"
        Output= 2
        self.assertEqual(Output,get_sol().numSplits(s))
    # def test_5(self):
    # def test_6(self):
