import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
    # https://www.youtube.com/watch?v=hqGa65Rp5LQ
    # https://www.youtube.com/watch?v=MqYLmIzl8sQ
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n=len(stones)
        summ = sum(stones)
        stones=['#']+stones

        dp =[[0]*(summ+1) for _ in range(n+1)]
        for i in range(n + 1):
            dp[i][0] = True
        for j in range(1, summ + 1):
            dp[0][j] = False
        for i in range(1, n + 1):
            for j in range(1, summ + 1):
                # If i'th element is excluded
                dp[i][j] = dp[i - 1][j]
                # If i'th element is included
                if stones[i] <= j:
                    dp[i][j] |= dp[i - 1][j - stones[i]]

        diff = float('inf')

        # Find the largest j such that dp[n][j]
        # is true where j loops from sum/2 t0 0
        for j in range(summ // 2, -1, -1):
            if dp[n][j] == True:
                diff = summ - (2 * j)
                break
        return diff
class tester(unittest.TestCase):
    def test_1(self):
        stones = [2,7,4,1,8,1]
        Output= 1
        self.assertEqual(Output,get_sol().lastStoneWeightII(stones))
    def test_2(self):
        stones = [31,26,33,21,40]
        Output= 5
        self.assertEqual(Output,get_sol().lastStoneWeightII(stones))
    def test_3(self):
        stones = [1,2]
        Output= 1
        self.assertEqual(Output,get_sol().lastStoneWeightII(stones))
    def test_4(self):
        stones = [2,6,4,1]
        Output= 1
        self.assertEqual(Output,get_sol().lastStoneWeightII(stones))
    # def test_5(self):
    # def test_6(self):
