from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-%3A)-(In-case-if-interviewer-twists-the-input)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        cur_buy_price=float('inf')
        total_profit=0
        for i in range(n):
            if prices[i]<cur_buy_price: # if price is lower buy it
                cur_buy_price=prices[i]
            else: # if price is higher sell it and buy it again
                profit=prices[i]-cur_buy_price
                cur_buy_price=prices[i]
                total_profit+=profit
        return total_profit
class Solution4:
    def maxProfit(self, A: List[int]) -> int:
        n=len(A)
        res=0
        i=0
        while i<n:
            while i+1<n and A[i+1]<A[i]:
                i+=1
            buy=A[i]
            while i+1<n and A[i+1]>A[i]:
                i+=1
            sell=A[i]
            res+=sell-buy
            i+=1
        return res
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                profit+=prices[i+1]-prices[i]
        return profit

class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        cur_max, max_so_far = 0, 0
        for i in range(1, len(prices)):
            temp = prices[i]-prices[i-1]
            cur_max = max(0, prices[i]-prices[i-1])
            max_so_far += cur_max
        return max_so_far

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(7, get_sol().maxProfit([7,1,5,3,6,4]))
    def test02(self):
        self.assertEqual(4, get_sol().maxProfit([1,2,3,4,5]))
    def test03(self):
        self.assertEqual(0, get_sol().maxProfit([7,6,4,3,1]))
