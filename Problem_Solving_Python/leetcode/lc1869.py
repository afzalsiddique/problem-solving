import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zeros=0
        max_zeros=-1
        ones=0
        max_ones=-1
        for c in s:
            if c=='0':
                zeros+=1
                max_zeros=max(max_zeros,zeros)
                ones=0
            else:
                ones+=1
                max_ones=max(max_ones,ones)
                zeros=0
        print(max_zeros,max_ones)
        return max_ones>max_zeros


class tester(unittest.TestCase):
    def test01(self):
        s = "1101"
        Output= True
        self.assertEqual(Output, get_sol().checkZeroOnes(s))
    def test02(self):
        s = "111000"
        Output= False
        self.assertEqual(Output, get_sol().checkZeroOnes(s))
    def test03(self):
        s = "110100010"
        Output= False
        self.assertEqual(Output, get_sol().checkZeroOnes(s))
