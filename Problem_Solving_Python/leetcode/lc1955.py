from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/count-number-of-special-subsequences/discuss/1375485/JavaC++Python-DP-Solution/1031931
    def countSpecialSubsequences(self, A: List[int]) -> int:
        M=10**9+7
        A=['dummy']+A
        n=len(A)
        dp=[0]*3
        for i in range(1,n):
            if A[i]==0:
                dp[0]=2*dp[0]+1
            elif A[i]==1:
                dp[1]=2*dp[1]+dp[0]
            else:
                dp[2]=2*dp[2]+dp[1]
            dp[0]%=M
            dp[1]%=M
            dp[2]%=M
        return dp[2]
class Solution2:
    def countSpecialSubsequences(self, A: List[int]) -> int:
        M=10**9+7
        A=['dummy']+A
        n=len(A)
        dp=[[0]*3 for _ in range(n)]
        for i in range(1,n):
            dp[i][0]=dp[i-1][0]
            dp[i][1]=dp[i-1][1]
            dp[i][2]=dp[i-1][2]
            if A[i]==0:
                dp[i][0]=2*dp[i][0]+1
            elif A[i]==1:
                dp[i][1]=2*dp[i][1]+dp[i][0]
            else:
                dp[i][2]=2*dp[i][2]+dp[i][1]
            dp[i][0]%=M
            dp[i][1]%=M
            dp[i][2]%=M
        return dp[-1][2]
class Solution3:
    # tle
    def countSpecialSubsequences(self, A: List[int]) -> int:
        MOD=10**9+7
        @cache
        def dfs(i,prev):
            if i==n:
                return prev==2
            res=0
            res=(res+dfs(i+1,prev))%MOD # skip it
            if prev==A[i]: # take the same element if it equals the prev -> [1,1]-> [1,1,1]
                res=(res+dfs(i+1,prev))%MOD
            if prev==A[i]-1: # take the next element if the prev element one less than the current element -> [1,1] -> [1,1,2]
                res= (res + dfs(i + 1, A[i])) % MOD
            return res

        n=len(A)
        return dfs(0,-1)

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(3, get_sol().countSpecialSubsequences([0,1,2,2]))
    def test02(self):
        self.assertEqual(0, get_sol().countSpecialSubsequences([2,2,0,0]))
    def test03(self):
        self.assertEqual(7, get_sol().countSpecialSubsequences([0,1,2,0,1,2]))
    # def test04(self):
