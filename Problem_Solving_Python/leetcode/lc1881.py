import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxValue(self, n: str, x: int) -> str:
        length = len(n)
        if n[0]!='-':
            i=0
            while i<length and int(n[i])>=x:
                i+=1
            n=n[:i]+str(x)+n[i:]
        else:
            i=1
            while i<length and int(n[i])<=x:
                i+=1
            n=n[:i]+str(x)+n[i:]
        return n


class tester(unittest.TestCase):
    def test1(self):
        n = "99"
        x = 9
        Output= "999"
        self.assertEqual(Output,get_sol().maxValue(n,x))
    def test2(self):
        n = "97"
        x = 8
        Output= "987"
        self.assertEqual(Output,get_sol().maxValue(n,x))
    def test3(self):
        n = "-13"
        x = 2
        Output= "-123"
        self.assertEqual(Output,get_sol().maxValue(n,x))
    def test4(self):
        n = "0"
        x = 2
        Output= "2"
        self.assertEqual(Output,get_sol().maxValue(n,x))
