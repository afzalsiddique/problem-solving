import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ENOUGH = 32
        a = bin(a)[2:]
        a = (ENOUGH-len(a)) * '0' + a
        b = bin(b)[2:]
        b = (ENOUGH-len(b)) * '0' + b
        c = bin(c)[2:]
        c = (ENOUGH-len(c)) * '0' + c
        d=[]
        for i in range(ENOUGH): # or operation
            if a[i]==b[i]=='0':
                d.append('0')
            else:
                d.append('1')
        d=''.join(d)
        # print(a)
        # print(b)
        # print(d)
        # print(c)
        res=0
        for i in range(ENOUGH):
            if c[i]==d[i]: continue
            if a[i]==b[i]=='1':
                res+=2
            else:
                res+=1
        return res

class Tester(unittest.TestCase):
    def test_1(self):
        a,b,c= 2,6,5
        Output= 3
        self.assertEqual(Output,get_sol().minFlips(a,b,c))
    def test_2(self):
        a,b,c= 4,2,7
        Output= 1
        self.assertEqual(Output,get_sol().minFlips(a,b,c))
    def test_3(self):
        a,b,c= 1,2,3
        Output= 0
        self.assertEqual(Output,get_sol().minFlips(a,b,c))
    def test_4(self):
        a,b,c= 7, 7, 7
        Output= 0
        self.assertEqual(Output,get_sol().minFlips(a,b,c))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
