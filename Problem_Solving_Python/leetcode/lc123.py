import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List


class Solution:
    # divide and conquer
    # https://www.youtube.com/watch?v=37s1_xBiqH0&t=854s
    # def maxProfit(self, prices: List[int]) -> int:

    def maxProfit(self, prices: List[int]) -> int:
        # https://www.youtube.com/watch?v=YAWRyWJalM0
        n=len(prices)
        buy1=float('inf')
        sell1=0
        buy2=float('inf')
        sell2=0
        for i in range(n):
            buy1=min(buy1,prices[i])
            sell1=max(sell1,prices[i]-buy1)
            buy2=min(buy2,prices[i]-sell1)
            sell2=max(sell2,prices[i]-buy2)
        return max(0,sell2)

    # state-machine. time O(n). space O(1)
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/149383/Easy-DP-solution-using-state-machine-O(n)-time-complexity-O(1)-space-complexity
    def maxProfit2(self, prices: List[int]) -> int:
        n=len(prices)
        buy1,sell1,buy2,sell2=float('-inf'),float('-inf'),float('-inf'),float('-inf')
        for i in range(n):
            buy1=max(buy1,-prices[i])
            sell1=max(sell1,buy1+prices[i])
            buy2=max(buy2,sell1-prices[i])
            sell2=max(sell2,buy2+prices[i])
        return max(0,sell2)


    # state-machine. time O(2^n)
    # https://www.youtube.com/watch?v=37s1_xBiqH0&t=320s
    def maxProfit3(self, prices: List[int]) -> int:
        dp={}
        n=len(prices)
        buy,sell,no_state='buy','sell','no_state'
        def helper(day, k, state):
            if day==n: return 0
            if k==0: return 0
            if (day, k, state) in dp: return dp[(day, k, state)]
            if state==buy:
                dp[day, k, state]=max(helper(day + 1, k - 1, sell) + prices[day], helper(day + 1, k, buy))
            elif state==sell:
                dp[day, k, state]=max(helper(day + 1, k, buy) - prices[day], helper(day + 1, k, sell))
            else:
                dp[day, k, state]=max(helper(day + 1, k, no_state), helper(day + 1, k, buy) - prices[day])
            return dp[day, k, state]

        return helper(0,2,no_state)

# TLE
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:

        def helper(prices: List[int]) -> int:
            n=len(prices)
            buy,sell=float('inf'),float('-inf')
            profit=0
            for i in range(n):
                if prices[i]<buy:
                    buy=prices[i]
                else:
                    sell=prices[i]
                    profit=max(profit,sell-buy)
            return profit

        n=len(prices)
        if n<4:
            return helper(prices)
        maxx=0
        option1=helper(prices)
        for i in range(2,n-1):
            option2=helper(prices[0:i])+helper(prices[i:])
            maxx=max(maxx,option2)
        return max(maxx,option1)

class tester(unittest.TestCase):
    def test1(self):
        prices = [3,3,5,0,0,3,1,4]
        Output= 6
        self.assertEqual(Output,Solution().maxProfit(prices))
    def test2(self):
        prices = [1,2,3,4,5]
        Output= 4
        self.assertEqual(Output,Solution().maxProfit(prices))
    def test3(self):
        prices = [7,6,4,3,1]
        Output= 0
        self.assertEqual(Output,Solution().maxProfit(prices))
    def test4(self):
        prices = [1]
        Output= 0
        self.assertEqual(Output,Solution().maxProfit(prices))
    def test5(self):
        prices = [1,2,3]
        Output= 2
        self.assertEqual(Output,Solution().maxProfit(prices))
