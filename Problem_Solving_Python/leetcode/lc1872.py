import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/stone-game-viii/discuss/1224640/C++Python-DP-O(N)-time-O(1)-space-(2-lines-1-line)/947881
    def stoneGameVIII(self, stones: List[int]) -> int:
        pre=list(itertools.accumulate(stones))

        n=len(stones)
        dp=[float('-inf')]*n
        dp[-2]=pre[n-1] # if there are two stones left take all stones
        for i in range(n-3,-1,-1):
            dp[i]=max(dp[i+1],pre[i+1]-dp[i+1])
        return dp[0]


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(5,get_sol().stoneGameVIII([-1,2,-3,4,-5]))
    def test2(self):
        self.assertEqual(13,get_sol().stoneGameVIII([7,-6,5,10,5,-2,-6]))
    def test3(self):
        self.assertEqual(-22,get_sol().stoneGameVIII([-10,-12]))
    def test4(self):
        self.assertEqual(38,get_sol().stoneGameVIII([25,-35,-37,4,34,43,16,-33,0,-17,-31,-42,-42,38,12,-5,-43,-10,-37,12]))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
