import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        n=len(s)
        l=0
        r=0
        res=0
        while r<n:
            while r<n and s[r]==s[l]:
                r+=1
            summ=0
            if r-l>1:
                maxx=float('-inf')
                for i in range(l,r):
                    summ+=cost[i]
                    maxx=max(cost[i],maxx)
                summ-=maxx # take the sum except the max cost
            res+=summ
            l=r
        return res

class tester(unittest.TestCase):
    def test_1(self):
        s = "abaac"
        cost = [1,2,3,4,5]
        Output= 3
        self.assertEqual(Output, get_sol().minCost(s,cost))
    def test_2(self):
        s = "abc"
        cost = [1,2,3]
        Output= 0
        self.assertEqual(Output, get_sol().minCost(s,cost))
    def test_3(self):
        s = "aabaa"
        cost = [1,2,3,4,1]
        Output= 2
        self.assertEqual(Output, get_sol().minCost(s,cost))
    def test_4(self):
        s = "bbbaaa"
        cost = [4,9,3,8,8,9]
        Output= 23
        self.assertEqual(Output, get_sol().minCost(s,cost))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):