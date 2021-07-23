import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/stone-game-ii/discuss/345230/JavaPython-DP-Solution/611761
    def stoneGameII(self, piles: List[int]) -> int:
        dp={}
        n=len(piles)
        cum_sum=piles[:]
        for i in range(n-2,-1,-1): cum_sum[i]+=cum_sum[i+1] # cumulative sum in reverse order
        def dfs(start, m):
            if start+2*m>=n: return cum_sum[start] # takes all the remaining stones
            if (start,m) in dp: return dp[start,m]
            res = 0
            total = cum_sum[start] # same as ->  total = sum(piles[start:])
            for i in range(1, 2*m+1):
                optima = dfs(start + i, max(m, i))
                res = max(res, total - optima)
            dp[start,m]=res
            return res

        return dfs(0, 1)

class tester(unittest.TestCase):
    def test_1(self):
        piles = [2,7,9,4,4]
        Output= 10
        self.assertEqual(Output, get_sol().stoneGameII(piles))
    def test_2(self):
        piles = [1,2,3,4,5,100]
        Output= 104
        self.assertEqual(Output, get_sol().stoneGameII(piles))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):