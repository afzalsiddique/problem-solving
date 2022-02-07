from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# https://www.youtube.com/watch?v=oDhu5uGq_ic

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        BOUGHT,SOLD=0,1
        @cache
        def helper(i, cnt, state):
            if i==n: return 0
            if cnt==0: return 0
            if state==BOUGHT:
                return max(helper(i + 1,cnt-1,1-state) + prices[i], helper(i + 1, cnt, state))
            return max(helper(i + 1,cnt,1-state) - prices[i], helper(i + 1, cnt, state))

        n=len(prices)
        return helper(0,k,SOLD)
class Solution3:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # https://www.youtube.com/watch?v=mFwf1YbH-Jk
        if k==0: return 0
        n=len(prices)
        # optimization
        # if n==0: return 0
        # if k>=n//2:
        #     return self.quick_solve(prices) # same as best time to buy and stock ii
        minp = [float('inf')] * k
        maxp = [0] * k
        for i in range(n):
            for j in range(k):
                if j>0:
                    minp[j] = min(minp[j], prices[i]-maxp[j-1]) # buy at lower price
                else: # first buy
                    minp[j]= min(minp[j],prices[i])
                maxp[j] = max(maxp[j], prices[i] - minp[j]) # sell at higher price
        return maxp[-1]

    def quick_solve(self, prices: List[int]) -> int:
        n=len(prices)
        if n==1:return 0
        cur_buy_price=prices[0]
        total_profit=0
        for i in range(1,n):
            if prices[i]<cur_buy_price: # if price is lower buy it
                cur_buy_price=prices[i]
            else: # if price is higher sell it and buy it again
                profit=prices[i]-cur_buy_price
                cur_buy_price=prices[i]
                total_profit+=profit
        return total_profit

# TLE at last test case. time O(k*n^2)
class Solution2:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        if n==0: return 0
        dp=[[float('-inf')] * n for _ in range(k + 1)]
        # max_profit could be by making no transaction at all. That's why k can be 0.
        for i in range(k + 1):
            dp[i][0]=0
        for j in range(n):
            dp[0][j]=0
        for i in range(1, k + 1):
            for j in range(1,n):
                for m in range(j):
                    option1=dp[i][j-1]
                    option2=prices[j]-prices[m]+dp[i-1][m]
                    dp[i][j]=max(dp[i][j],option1,option2)
        return dp[-1][-1]

class tester(unittest.TestCase):
    def test1(self):
        k = 2
        prices = [2,4,1]
        Output= 2
        self.assertEqual(Output,get_sol().maxProfit(k,prices))
    def test2(self):
        k = 2
        prices = [3,2,6,5,0,3]
        Output =7
        self.assertEqual(Output,get_sol().maxProfit(k,prices))
    def test3(self):
        k = 3
        prices = [2,5,7,1,4,3,1,3]
        Output =10
        self.assertEqual(Output,get_sol().maxProfit(k,prices))
    def test4(self):
        k = 2
        prices = []
        Output =0
        self.assertEqual(Output,get_sol().maxProfit(k,prices))
    def test5(self):
        k = 0
        prices = [1,2]
        Output =0
        self.assertEqual(Output,get_sol().maxProfit(k,prices))
