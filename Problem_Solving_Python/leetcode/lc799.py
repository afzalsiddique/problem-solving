import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        BIG = 101
        CAPACITY=1
        dp=[[0]*(BIG+1) for _ in range(BIG+1)]
        dp[0][0]=poured
        for i in range(BIG):
            for j in range(i+1):
                if dp[i][j]>CAPACITY:
                    extra=dp[i][j]-CAPACITY
                    dp[i+1][j]+=extra/2
                    dp[i+1][j+1]+=extra/2
                    dp[i][j]=CAPACITY
        return dp[query_row][query_glass]

class tester(unittest.TestCase):
    def test_1(self):
        poured = 1
        query_row = 1
        query_glass = 1
        Output= 0.00000
        self.assertEqual(Output,get_sol().champagneTower(poured,query_row,query_glass))
    def test_2(self):
        poured = 2
        query_row = 1
        query_glass = 1
        Output= 0.50000
        self.assertEqual(Output,get_sol().champagneTower(poured,query_row,query_glass))
    def test_3(self):
        poured = 100000009
        query_row = 33
        query_glass = 17
        Output= 1.00000
        self.assertEqual(Output,get_sol().champagneTower(poured,query_row,query_glass))
    # def test_4(self):
    # def test_5(self):
