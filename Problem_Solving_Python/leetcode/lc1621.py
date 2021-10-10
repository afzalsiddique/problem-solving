import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # tle
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9+7
        START,END=True,False
        def dfs(i, k, state):
            if (i,k) in dp: return dp[i,k,state]
            if i==n: return 0
            if k==0: return 1 # found a way
            ans= dfs(i + 1, k, state) # skip this point
            if state==START:
                ans+=dfs(i+1,k,END) # take the ith point as start
            else: # state==END
                # take the ith point as end. We can have ith point as a starting point. Because
                # starting point can overlap with the last end point. So dont increment i
                ans+=dfs(i,k-1,START)
            ans%=MOD
            dp[i,k,state]=ans
            return ans

        dp={}
        return dfs(0,k,START)

class MyTestCase(unittest.TestCase):
    def test1(self):
        n,k = 4,  2
        Output= 5
        self.assertEqual(Output, get_sol().numberOfSets(n,k))
    def test2(self):
        n,k = 3,  1
        Output= 3
        self.assertEqual(Output, get_sol().numberOfSets(n,k))
    def test3(self):
        n,k = 30,  7
        Output= 796297179
        self.assertEqual(Output, get_sol().numberOfSets(n,k))
    def test4(self):
        n,k = 5,  3
        Output= 7
        self.assertEqual(Output, get_sol().numberOfSets(n,k))
    def test5(self):
        n,k = 3,  2
        Output= 1
        self.assertEqual(Output, get_sol().numberOfSets(n,k))
    def test6(self):
        n,k = 251, 234
        Output= 1
        self.assertEqual(Output, get_sol().numberOfSets(n,k))

    # def test7(self):
