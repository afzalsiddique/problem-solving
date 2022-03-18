from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# https://www.youtube.com/watch?v=4wNXkhAky3s&t=1164s
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        BUY,SELL=0,1
        @cache
        def recur(i,state):
            if i>=n: return 0
            if state==BUY:
                option1=prices[i]+recur(i+2,SELL)
                option2=recur(i+1,BUY)
            else:
                option1=-prices[i]+recur(i+1,BUY)
                option2=recur(i+1,SELL)
            return max(option1,option2)

        n=len(prices)
        return recur(0,SELL)
class Solution3:
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        in_hand,no_stock,cooldown = 1,0,-1
        dp = {}
        def f(i, state):
            if i == n: return 0
            if (i, state) in dp: return dp[(i, state)]
            if state == cooldown: # after cooldown go to no_stock state
                dp[(i, state)] = f(i + 1, no_stock)
            if state == no_stock:
                dp[(i, state)] = max(f(i + 1, no_stock), f(i + 1, in_hand) - prices[i])
            if state == in_hand:
                dp[(i, state)] = max(prices[i] + f(i + 1, cooldown), f(i + 1, in_hand))
            return dp[(i, state)]
        return f(0,0)

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        no_stock,in_hand,sold =[0]*n,[0]*n,[0]*n
        in_hand[0]=0-prices[0]
        for i in range(1,n):
            no_stock[i]=max(no_stock[i-1],sold[i-1])
            in_hand[i]=max(in_hand[i-1],no_stock[i-1]-prices[i])
            sold[i]=in_hand[i-1]+prices[i]
        return max(no_stock[-1],in_hand[-1],sold[-1])

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(3,get_sol().maxProfit([1,2,3,0,2]))
