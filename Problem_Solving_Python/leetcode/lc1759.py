import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def countHomogenous(self, s: str) -> int:
        length=len(s)
        MOD=10**9+7
        left=0;right=0
        res=0
        while right<length:
            while right<length and s[left]==s[right]:
                right+=1
            n=right-left
            res+=n*(n+1)//2
            res%=MOD
            left=right
        return res

class MyTestCase(unittest.TestCase):
    def test_1(self):
        s = "abbcccaa"
        Output= 13
        self.assertEqual(Output, get_sol().countHomogenous(s))
    def test_2(self):
        s = "xy"
        Output= 2
        self.assertEqual(Output, get_sol().countHomogenous(s))
    def test_3(self):
        s = "zzzzz"
        Output= 15
        self.assertEqual(Output, get_sol().countHomogenous(s))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
