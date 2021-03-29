# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-%3A)-(In-case-if-interviewer-twists-the-input)
import unittest
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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

    def test_1(self):
        solution = Solution()
        self.assertEqual(7, solution.maxProfit([7,1,5,3,6,4]))

    def test_2(self):
        solution = Solution()
        self.assertEqual(4, solution.maxProfit([1,2,3,4,5]))

    def test_3(self):
        solution = Solution()
        self.assertEqual(0, solution.maxProfit([7,6,4,3,1]))
