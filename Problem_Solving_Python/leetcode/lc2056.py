import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n=len(s)
        left_candle = [-1]*n
        right_candle = [-1]*n
        res = []
        for i in range(n):
            if s[i]=='|':
                left_candle[i]=i
            elif i>0:
                left_candle[i]=left_candle[i-1]
        for i in range(n-1,-1,-1):
            if s[i]=='|':
                right_candle[i]=i
            elif i<n-1:
                right_candle[i]=right_candle[i+1]

        s = [c=='*' for c in s]
        pre_sum = list(itertools.accumulate(s))
        for left,right in queries:
            left_boundary = right_candle[left]
            right_boundary = left_candle[right]
            count = pre_sum[right_boundary]-pre_sum[left_boundary]
            res.append(max(count,0))
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        s,queries = "**|**|***|",  [[2,5],[5,9]]
        Output= [2,3]
        self.assertEqual(Output, get_sol().platesBetweenCandles(s,queries))
    def test2(self):
        s,queries = "***|**|*****|**||**|*",  [[1,17],[4,5],[14,17],[5,11],[15,16]]
        Output= [9,0,0,0,0]
        self.assertEqual(Output, get_sol().platesBetweenCandles(s,queries))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
