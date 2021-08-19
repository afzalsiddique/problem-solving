import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/convert-to-base-2/discuss/265507/JavaC%2B%2BPython-2-lines-Exactly-Same-as-Base-2
    def baseNeg2(self, n: int) -> str:
        if n==0: return '0'
        res=[]
        while n:
            res.append(n%2)
            n = -(n//2)
            # n= n//(-2) # does not work
        return ''.join(list(map(str,res[::-1])))
class Solution2:
    def baseNeg2(self, n: int) -> str:
        if n==0: return '0'
        res=[]
        while n:
            res.append(n&1)
            n = -(n>>1)
        return ''.join(list(map(str,res[::-1])))



class Tester(unittest.TestCase):
    def test_1(self):
        n = 2
        Output= "110"
        self.assertEqual(Output,get_sol().baseNeg2(n))
    def test_2(self):
        n = 3
        Output= "111"
        self.assertEqual(Output,get_sol().baseNeg2(n))
    def test_3(self):
        n = 4
        Output= "100"
        self.assertEqual(Output,get_sol().baseNeg2(n))
    def test_4(self):
        n = 0
        Output= "0"
        self.assertEqual(Output,get_sol().baseNeg2(n))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):