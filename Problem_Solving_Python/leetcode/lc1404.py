import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def numSteps(self, s: str) -> int:
        s=deque(s)
        steps=0
        while True:
            if len(s)==1 and s[0]=='1':
                return steps
            if s[-1]=='0':
                s.pop()
            elif s[-1]=='1':
                i=len(s)-1
                while i>=0 and s[i]=='1':
                    s[i]='0'
                    i-=1
                if i==-1:
                    s.appendleft('1')
                else:
                    s[i]='1'
            steps+=1



class Tester(unittest.TestCase):
    def test1(self):
        s = "1101"
        Output= 6
        self.assertEqual(Output,get_sol().numSteps(s))
    def test2(self):
        s = "10"
        Output= 1
        self.assertEqual(Output,get_sol().numSteps(s))
    def test3(self):
        s = "1"
        Output= 0
        self.assertEqual(Output,get_sol().numSteps(s))
    def test4(self):
        s = "11001"
        Output= 8
        self.assertEqual(Output,get_sol().numSteps(s))
    # def test5(self):
    # def test6(self):
    # def test7(self):
