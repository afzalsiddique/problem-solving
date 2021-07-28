import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        # print(s1)
        # print(s2)
        flag1=True
        flag2=True
        for i in range(len(s1)):
            if s1[i]<s2[i]:
                flag1=False
                break
        for i in range(len(s1)):
            if s2[i]<s1[i]:
                flag2=False
                break
        return flag1 or flag2

class tester(unittest.TestCase):
    def test_1(self):
        s1 = "abc"
        s2 = "xya"
        Output= True
        self.assertEqual(Output,get_sol().checkIfCanBreak(s1,s2))
    def test_2(self):
        s1 = "abe"
        s2 = "acd"
        Output= False
        self.assertEqual(Output,get_sol().checkIfCanBreak(s1,s2))
    def test_3(self):
        s1 = "leetcodee"
        s2 = "interview"
        Output= True
        self.assertEqual(Output,get_sol().checkIfCanBreak(s1,s2))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):