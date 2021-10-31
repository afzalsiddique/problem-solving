import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a,b = num1.split('+')
        a = int(a)
        b=int(b[:-1])

        c,d = num2.split('+')
        c = int(c)
        d=int(d[:-1])

        e = a*c - b*d
        f = a*d + b*c
        e,f = str(e), str(f)
        return e + "+" + f + "i"

class MyTestCase(unittest.TestCase):
    def test1(self):
        num1,num2 = "1+1i",  "1+1i"
        Output= "0+2i"
        self.assertEqual(Output, get_sol().complexNumberMultiply(num1,num2))
    def test2(self):
        num1,num2 = "1+-1i",  "1+-1i"
        Output= "0+-2i"
        self.assertEqual(Output, get_sol().complexNumberMultiply(num1,num2))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
