from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-%3A)-(In-case-if-interviewer-twists-the-input)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        buy,sell=float('inf'),float('-inf')
        max_profit=0
        for i in range(n):
            if prices[i]<buy: # buy when price is less
                buy=prices[i]
            else: # sell when price is higher
                sell=prices[i]
                max_profit=max(max_profit,sell-buy) # update profit
        return max_profit
class Solution5:
    def maxProfit(self, prices: List[int]) -> int:
        buying=float('inf')
        res=float('-inf')
        for selling in prices:
            buying=min(buying,selling)
            res=max(res,selling-buying)
        return res

# using range
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        def helper(lo, hi) -> int:
            if lo>hi: return 0
            buy,sell=float('inf'),float('-inf')
            max_profit=0
            for lo in range(lo,hi+1): # hi is inclusive
                if prices[lo]<buy:
                    buy=prices[lo]
                else:
                    sell=prices[lo]
                    max_profit=max(max_profit,sell-buy)
            return max_profit

        return helper(0,len(prices)-1)
class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        cur_buy_price = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            profit = max(profit, prices[i]-cur_buy_price)
            cur_buy_price = min(cur_buy_price, prices[i])
        return profit

class Solution4:
    def maxProfit(self, prices: List[int]) -> int:
        cur_max, max_so_far = 0, 0
        for i in range(1, len(prices)):
            temp = prices[i]-prices[i-1]
            cur_max = max(0, cur_max + prices[i]-prices[i-1])
            max_so_far = max(max_so_far, cur_max)
        return max_so_far
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(5, get_sol().maxProfit([7,1,5,3,6,4]))
    def test02(self):
        self.assertEqual(0, get_sol().maxProfit([7,6,4,3,1]))
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
