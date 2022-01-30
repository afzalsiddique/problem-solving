from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # tabulation dp
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        coins = [0] + coins
        dp=[[None]*(amount+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1
        for j in range(1,amount+1):
            dp[0][j]=0
        for i in range(1,n+1):
            for j in range(1,amount+1):
                if j<coins[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-coins[i]]
        return dp[-1][-1]
class Solution2:
    # knapsack
    # beats 62% in runtime
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)
        n=len(coins)
        dp ={}
        def f(i, target):
            if target == 0 : return 1
            if target < 0: return 0
            if i>=n: return 0
            if (i,target) in dp: return dp[(i,target)]
            ans = f(i, target - coins[i]) + f(i + 1, target)
            dp[(i,target)]=ans
            return ans

        return f(0,amount)
class Solution3:
    # recursive knapsack
    # beats 62% in runtime
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        coins.sort(reverse=True)
        @cache
        def f(i, target):
            if target == 0 : return 1
            if target < 0: return 0
            if i>=n: return 0
            return f(i, target - coins[i]) + f(i + 1, target)

        return f(0,amount)
class Solution4:
    # recursive dp
    # beats 20% in runtime
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        coins.sort(reverse=True)
        dp={}
        def helper(idx,target):
            if target<0: return 0
            if target==0: return 1
            if (idx,target) in dp: return dp[(idx,target)]
            cnt=0
            for i in range(idx,n):
                cnt+=helper(i,target-coins[i])
            dp[(idx,target)]=cnt
            return cnt
        return helper(0,amount)
class MyTestCase(unittest.TestCase):
    def test01(self):
        amount = 5
        coins = [1,2,5]
        actual = get_sol().change(amount, coins)
        expected = 4
        self.assertEqual(expected, actual)
    def test02(self):
        amount = 3
        coins = [2]
        actual = get_sol().change(amount, coins)
        expected = 0
        self.assertEqual(expected, actual)
    def test03(self):
        amount = 10
        coins = [10]
        actual = get_sol().change(amount, coins)
        expected = 1
        self.assertEqual(expected, actual)
    def test4(self):
        self.assertEqual(1,get_sol().change(0,[]))