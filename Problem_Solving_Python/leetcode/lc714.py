import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class Solution:
    # time O(n) space O(1)
    def maxProfit(self, prices, fee):
        sold, bought = 0, -prices[0]
        for i in range(1, len(prices)):
            sold = max(sold, bought + prices[i] - fee)
            bought = max(bought, sold - prices[i])
        return sold
    def maxProfit2(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        bought,sold = True,False
        dp={}
        def helper(i, state):
            if i==n: return 0
            if (i, state) in dp: return dp[(i, state)]
            if state==bought:
                option1 = helper(i+1,bought)
                option2 = helper(i+1,sold)+prices[i]-fee
            else: # elif state==sold:
                option1 = helper(i+1,sold)
                option2 = helper(i+1,bought)-prices[i]
            dp[(i,state)]=max(option1,option2)
            return dp[(i,state)]

        return helper(0,sold)

class tester(unittest.TestCase):
    def test1(self):
        prices = [1,3,2,8,4,9]
        fee = 2
        Output= 8
        self.assertEqual(Output,Solution().maxProfit(prices,fee))
    def test2(self):
        prices = [1,3,7,5,10,3]
        fee = 3
        Output= 6
        self.assertEqual(Output,Solution().maxProfit(prices,fee))