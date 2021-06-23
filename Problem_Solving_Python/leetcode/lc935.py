import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/knight-dialer/discuss/189252/O(logN)
    # time O(n) space O(1)
    MOD = int(1e9+7)
    def knightDialer(self, N):
        neighbors = {
            0:(4,6),
            1:(6,8),
            2:(7,9),
            3:(4,8),
            4:(0,3,9),
            5:(),
            6:(0,1,7),
            7:(2,6),
            8:(1,3),
            9:(2,4)
        }
        counts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        for _ in range(N-1):
            next_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # required for simultaneous update
            for src_key in neighbors:
                for dst_key in neighbors[src_key]:
                    next_counts[dst_key] = (next_counts[dst_key] + counts[src_key]) % (10**9 + 7)
            counts = next_counts
        return sum(counts) % (10**9 + 7)
class Solution2:
    def knightDialer(self, n: int) -> int:
        row,col=4,3
        MOD = int(1e9+7)
        dir = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
        dp = {}
        def dfs(i,j,n):
            if not 0<=i<row or not 0<=j<col: return 0
            if i==3 and j!=1: return 0 # for "#", "*"
            if n==1: return 1
            if (i,j,n) in dp: return dp[i,j,n]
            ans = 0
            for di,dj in dir:
                new_i,new_j=i+di,j+dj
                ans+=dfs(new_i,new_j,n-1)
            dp[i,j,n]=ans
            return ans % MOD

        ans = 0
        for i in range(row):
            for j in range(col):
                ans+=dfs(i,j,n) % MOD
        return ans % MOD

class tester(unittest.TestCase):
    def test_01(self):
        n = 1
        Output= 10
        self.assertEqual(Output,get_sol().knightDialer(n))
    def test_02(self):
        n = 2
        Output= 20
        self.assertEqual(Output,get_sol().knightDialer(n))
    def test_03(self):
        n = 3
        Output= 46
        self.assertEqual(Output,get_sol().knightDialer(n))
    def test_04(self):
        n = 4
        Output= 104
        self.assertEqual(Output,get_sol().knightDialer(n))
    def test_05(self):
        print("works in OJ")
        n = 3131
        Output= 136006598
        self.assertEqual(Output,get_sol().knightDialer(n))