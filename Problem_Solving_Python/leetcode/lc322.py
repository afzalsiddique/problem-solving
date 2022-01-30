from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # recursive
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(i,target):
            if target==0:
                return 0
            if target<0:
                return float('inf')
            if i==len(coins):
                return float('inf')
            option1=1+dp(i,target-coins[i])
            option2=dp(i+1,target)
            return min(option1,option2)

        coins.sort(reverse=True)
        res= dp(0,amount)
        return res if res!=float('inf') else -1
class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        coins = [0] + coins
        dp=[[None]*(amount+1) for _ in range(n+1)]
        for j in range(amount+1):
            dp[0][j]=float('inf')
        for i in range(n+1):
            dp[i][0]=0
        for i in range(1,n+1):
            for j in range(1,amount+1):
                if j<coins[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i]])
        return dp[-1][-1] if dp[-1][-1]!=float('inf') else -1



class MyTestCase(unittest.TestCase):
    def test01(self):
        coins = [1,2,5]
        amount = 11
        expected = 3
        actual = get_sol().coinChange(coins, amount)
        self.assertEqual(expected, actual)
    def test02(self):
        coins = [2]
        amount = 3
        expected = -1
        actual = get_sol().coinChange(coins, amount)
        self.assertEqual(expected, actual)
    def test03(self):
        coins = [1]
        amount = 0
        expected = 0
        actual = get_sol().coinChange(coins, amount)
        self.assertEqual(expected, actual)
    def test04(self):
        coins = [1]
        amount = 1
        expected = 1
        actual = get_sol().coinChange(coins, amount)
        self.assertEqual(expected, actual)
    def test05(self):
        coins = [1]
        amount = 2
        expected = 2
        actual = get_sol().coinChange(coins, amount)
        self.assertEqual(expected, actual)