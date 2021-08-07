import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a,b):
            if b>a: return gcd(b,a)
            if b==0: return a
            return gcd(a-b,b)

        res=set()
        for nume in range(1,n):
            for deno in range(nume+1,n+1):
                div = gcd(nume,deno)
                res.add(str(nume//div)+"/"+str(deno//div))
        return list(res)
class Tester(unittest.TestCase):
    def test_1(self):
        n = 2
        Output= sorted(["1/2"])
        actual=sorted(get_sol().simplifiedFractions(n))
        self.assertEqual(Output,actual)
    def test_2(self):
        n = 3
        Output= sorted(["1/2","1/3","2/3"])
        actual=sorted(get_sol().simplifiedFractions(n))
        self.assertEqual(Output,actual)
    def test_3(self):
        n = 4
        Output= sorted(["1/2","1/3","1/4","2/3","3/4"])
        actual=sorted(get_sol().simplifiedFractions(n))
        self.assertEqual(Output,actual)
    def test_4(self):
        n = 1
        Output= []
        actual=sorted(get_sol().simplifiedFractions(n))
        self.assertEqual(Output,actual)
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):