import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # Sort tokens.
    # Buy at the cheapest and sell at the most expensive.
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        money=power
        prices=tokens


        maxx=0
        no_of_items=0
        prices.sort()
        i,j=0,len(prices)-1
        while i<=j:
            if money>=prices[i]: # buy
                money-=prices[i]
                no_of_items+=1
                maxx=max(maxx,no_of_items)
                i+=1
            else: # try to sell
                if no_of_items==0: break # cannot sell
                money+=prices[j] # we can sell items which we have never bought
                no_of_items-=1
                j-=1
        return maxx
class tester(unittest.TestCase):
    def test_1(self):
        tokens = [100]
        power = 50
        Output= 0
        self.assertEqual(Output,get_sol().bagOfTokensScore(tokens,power))
    def test_2(self):
        tokens = [100,200]
        power = 150
        Output= 1
        self.assertEqual(Output,get_sol().bagOfTokensScore(tokens,power))
    def test_3(self):
        tokens = [100,200,300,400]
        power = 200
        Output= 2
        self.assertEqual(Output,get_sol().bagOfTokensScore(tokens,power))
    # def test_4(self):
    # def test_5(self):
