import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        zero,one,two=0,0,0
        for s in stones:
            if s%3==0: zero+=1
            elif s%3==1: one+=1
            else: two+=1

        if zero%2==0:
            if min(one,two)==0: return False
            return True # pick stone from the smaller pile
        else:
            if abs(one-two)<=2:
                return False
            return True # pick stone from the larger pile


class MyTestCase(unittest.TestCase):
    def test1(self):
        stones = [2,1]
        Output= True
        self.assertEqual(Output, get_sol().stoneGameIX(stones))
    def test2(self):
        stones = [2]
        Output= False
        self.assertEqual(Output, get_sol().stoneGameIX(stones))
    def test3(self):
        stones = [5,1,2,4,3]
        Output= False
        self.assertEqual(Output, get_sol().stoneGameIX(stones))
    def test4(self):
        stones = [2,3,1]
        Output= False
        self.assertEqual(Output, get_sol().stoneGameIX(stones))
    def test5(self):
        stones = [2,2,3]
        Output= False
        self.assertEqual(Output, get_sol().stoneGameIX(stones))
    def test6(self):
        stones = [15,20,10,13,14,15,5,2,3]
        Output= False
        self.assertEqual(Output, get_sol().stoneGameIX(stones))
    def test7(self):
        stones = [20,3,20,17,2,12,15,17,4]
        Output= True
        self.assertEqual(Output, get_sol().stoneGameIX(stones))
