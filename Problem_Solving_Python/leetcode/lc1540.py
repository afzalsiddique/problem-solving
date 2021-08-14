import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        n,m=len(s),len(t)
        if n!=m: return False
        NUM=26
        pointers=[i for i in range(NUM)]
        for i in range(n):
            diff=(ord(t[i])-ord(s[i]))%NUM
            if diff!=0:
                if pointers[diff]>k: return False
                pointers[diff]+=NUM
        return True

class MyTestCase(unittest.TestCase):
    def test_1(self):
        s,t,k= "input","ouput", 9
        Output= True
        self.assertEqual(Output, get_sol().canConvertString(s,t,k))
    def test_2(self):
        s,t,k= "abc","bcd", 10
        Output= False
        self.assertEqual(Output, get_sol().canConvertString(s,t,k))
    def test_3(self):
        s,t,k= "aab","bbb", 27
        Output= True
        self.assertEqual(Output, get_sol().canConvertString(s,t,k))
    def test_4(self):
        s,t,k= "abc", "abcd", 1000
        Output= False
        self.assertEqual(Output, get_sol().canConvertString(s,t,k))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):