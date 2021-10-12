import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=3M_lU2b1N9I
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        MOD = 10**9+7
        n=len(nextVisit)
        dp=[0]*n
        for i in range(1,n):
            if nextVisit[i-1]==i-1:
                dp[i] = dp[i-1] + 2
            else:
                dp[i] = 2*dp[i-1] - dp[nextVisit[i-1]] + 2
        return dp[-1]%MOD

class MyTestCase(unittest.TestCase):
    def test1(self):
        nextVisit = [0,0]
        Output= 2
        self.assertEqual(Output, get_sol().firstDayBeenInAllRooms(nextVisit))
    def test2(self):
        nextVisit = [0,0,2]
        Output= 6
        self.assertEqual(Output, get_sol().firstDayBeenInAllRooms(nextVisit))
    def test3(self):
        nextVisit = [0,1,2,0]
        Output= 6
        self.assertEqual(Output, get_sol().firstDayBeenInAllRooms(nextVisit))
    def test4(self):
        nextVisit = [0,0,0,0,0,0,0,0,0,9,1,8]
        Output= 2048
        self.assertEqual(Output, get_sol().firstDayBeenInAllRooms(nextVisit))
    # def test5(self):
    # def test6(self):
