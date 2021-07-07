import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dp={1:0}
        def f(x):
            if x in dp: return dp[x]
            if x%2:
                ans=1+f(3*x+1)
            else:
                ans=1+f(x//2)
            dp[x]=ans
            return ans

        li=[]
        for x in range(lo,hi+1):
            f(x)
            li.append(x)
        li.sort(key=lambda x:dp[x])
        return li[k-1]

class tester(unittest.TestCase):
    def test_1(self):
        lo = 12
        hi = 15
        k = 2
        Output= 13
        self.assertEqual(Output,get_sol().getKth(lo,hi,k))
    def test_2(self):
        lo = 1
        hi = 1
        k = 1
        Output= 1
        self.assertEqual(Output,get_sol().getKth(lo,hi,k))
    def test_3(self):
        lo = 7
        hi = 11
        k = 4
        Output= 7
        self.assertEqual(Output,get_sol().getKth(lo,hi,k))
    def test_4(self):
        lo = 10
        hi = 20
        k = 5
        Output= 13
        self.assertEqual(Output,get_sol().getKth(lo,hi,k))
    def test_5(self):
        lo = 1
        hi = 1000
        k = 777
        Output= 570
        self.assertEqual(Output,get_sol().getKth(lo,hi,k))
    # def test_6(self):

