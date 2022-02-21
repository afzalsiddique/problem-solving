from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # tle
    def superEggDrop(self, k: int, n: int) -> int:
        @cache
        def drop(eggs, floors_left):
            if floors_left==0: return 0
            if floors_left==1: return 1
            if eggs==1: # if we are left with only one egg, we need to check for each floor
                return floors_left
            minn = float('inf')
            for f in range(1, floors_left + 1):
                minn = min(minn, 1 + max(drop(eggs - 1, f - 1), drop(eggs, floors_left - f)))
            return minn

        return drop(k, n)
class Solution2:
    # tle
    def superEggDrop(self, k: int, n: int) -> int:
        dp=[[float('inf')] * (n+1) for _ in range(k+1)]
        for i in range(1, k+1):
            dp[i][0] = 0
            dp[i][1] = 1
        for j in range(1, n+1):
            dp[1][j] = j

        for egg in range(2, k+1):
            for floors_left in range(2, n+1):
                for f in range(1, floors_left+1):
                    dp[egg][floors_left] = min(dp[egg][floors_left], 1 + max(dp[egg-1][f-1], dp[egg][floors_left-f]))
        return dp[k][n]
class Solution3:
    # https://leetcode.com/problems/super-egg-drop/discuss/158974/C%2B%2BJavaPython-2D-and-1D-DP-O(KlogN)
    # dp array could be reduced to 1d
    def superEggDrop(self, k, n):
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for moves in range(1, n + 1):
            for eggs_left in range(1, k + 1):
                dp[moves][eggs_left] = dp[moves - 1][eggs_left - 1] + dp[moves - 1][eggs_left] + 1
            if dp[moves][k] >= n: return moves
class Solution4:
    # https://leetcode.com/problems/super-egg-drop/discuss/705835/Python-DP-Bottom-up-%2B-Top-down
    # https://www.youtube.com/watch?v=xsOCvSiSrSs
    # Time O(KN log(N)) Space O(KN)
    def superEggDrop(self, K: int, N: int) -> int:
        @cache
        def dp(eggsLeft, moves):
            if eggsLeft == 1: return moves
            if moves == 1: return 1
            return dp(eggsLeft - 1, moves - 1) + dp(eggsLeft, moves - 1) + 1

        l, r = 1, N
        while l <= r:
            # while l < r: # group 1. uncomment all group 1
            mid = (l+r) // 2
            if dp(K, mid) >= N:
                r = mid - 1
                # r = mid # group 1
            else:
                l = mid + 1
        return l
class Solution5:
    # https://leetcode.com/problems/super-egg-drop/discuss/705835/Python-DP-Bottom-up-%2B-Top-down
    # https://www.youtube.com/watch?v=xsOCvSiSrSs
    # Bottom up: Time O(Klog(N)) Space O(K)
    def superEggDrop(self, K: int, N: int) -> int:
        dp, newDp = {}, {}
        for m in range(1, N+1):
            for k in range(1, K+1):
                if m == 1: newDp[k] = 1
                elif k == 1: newDp[k] = m
                else:
                    newDp[k] = dp[k-1] + dp[k] + 1
                if newDp[k] >= N:
                    return m
            dp, newDp = newDp, {}
class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, get_sol().superEggDrop(1, 2))
    def test2(self):
        self.assertEqual(3, get_sol().superEggDrop(2, 6))
    def test3(self):
        self.assertEqual(4, get_sol().superEggDrop(3, 14))
    def test4(self):
        self.assertEqual(16, get_sol().superEggDrop(4,2000))
    def test5(self):
        self.assertEqual(14, get_sol().superEggDrop(100,10000))
    # def test6(self):
    # def test7(self):
