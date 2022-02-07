from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution3()

class Solution:
    # divide and conquer
    # https://www.youtube.com/watch?v=37s1_xBiqH0&t=854s
    # def maxProfit(self, prices: List[int]) -> int:
    pass

class Solution5:
    def maxProfit(self, prices: List[int]) -> int:
        # https://www.youtube.com/watch?v=YAWRyWJalM0
        n=len(prices)
        buy1=float('inf')
        sell1=0
        buy2=float('inf')
        sell2=0
        for i in range(n):
            buy1=min(buy1,prices[i])
            sell1=max(sell1,prices[i]-buy1) # profit after first selling
            buy2=min(buy2,prices[i]-sell1)
            sell2=max(sell2,prices[i]-buy2)
        return sell2

class Solution2:
    # state-machine. time O(n). space O(1)
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/149383/Easy-DP-solution-using-state-machine-O(n)-time-complexity-O(1)-space-complexity
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        buy1,sell1,buy2,sell2=float('-inf'),float('-inf'),float('-inf'),float('-inf')
        for i in range(n):
            buy1=max(buy1,-prices[i])
            sell1=max(sell1,buy1+prices[i])
            buy2=max(buy2,sell1-prices[i])
            sell2=max(sell2,buy2+prices[i])
        return max(0,sell2)


class Solution3:
    # state-machine. time O(n)
    # https://www.youtube.com/watch?v=37s1_xBiqH0&t=320s
    def maxProfit(self, prices: List[int]) -> int:
        BOUGHT,SOLD=0,1
        @cache
        def helper(i, cnt, state):
            if i==n: return 0
            if cnt==0: return 0
            if state==BOUGHT:
                return max(helper(i + 1,cnt-1,1-state) + prices[i], helper(i + 1, cnt, state))
            return max(helper(i + 1,cnt,1-state) - prices[i], helper(i + 1, cnt, state))

        n=len(prices)
        return helper(0,2,SOLD)

class Solution4:
    # TLE
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
    def test01(self):
        prices = [3,3,5,0,0,3,1,4]
        Output= 6
        self.assertEqual(Output,get_sol().maxProfit(prices))
    def test02(self):
        prices = [1,2,3,4,5]
        Output= 4
        self.assertEqual(Output,get_sol().maxProfit(prices))
    def test03(self):
        prices = [7,6,4,3,1]
        Output= 0
        self.assertEqual(Output,get_sol().maxProfit(prices))
    def test04(self):
        prices = [1]
        Output= 0
        self.assertEqual(Output,get_sol().maxProfit(prices))
    def test05(self):
        prices = [1,2,3]
        Output= 2
        self.assertEqual(Output,get_sol().maxProfit(prices))
    def test06(self):
        self.assertEqual(4,get_sol().maxProfit([1,5]))
    def test07(self):
        self.assertEqual(0,get_sol().maxProfit([5,1]))
