import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp={}
        MOD = 10**9+7
        def helper(i,j,moves):
            if (i,j,moves) in dp: return dp[i,j,moves]
            if not 0<=i<m or not 0<=j<n:
                return 1
            if moves==N: return 0
            ans=0
            for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ans+=helper(i+di,j+dj,moves+1)
                ans%=MOD
            dp[i,j,moves]=ans
            return ans

        return helper(i,j,0)

class MyTestCase(unittest.TestCase):
    def test_01(self):
        m = 2
        n = 2
        N = 2
        i = 0
        j = 0
        Output= 6
        self.assertEqual(Output,get_sol().findPaths(m,n,N,i,j))
    def test_02(self):
        m = 1
        n = 3
        N = 3
        i = 0
        j = 1
        Output= 12
        self.assertEqual(Output,get_sol().findPaths(m,n,N,i,j))
    def test_03(self):
        m=8
        n=7
        N=16
        i=1
        j=5
        Output= 102984580
        self.assertEqual(Output,get_sol().findPaths(m,n,N,i,j))
    def test_04(self):
        m=36
        n=5
        N=50
        i=15
        j=3
        Output= 390153306
    # def test_05(self):
    # def test_06(self):
    # def test_07(self):

