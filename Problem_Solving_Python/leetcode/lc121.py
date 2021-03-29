# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-%3A)-(In-case-if-interviewer-twists-the-input)
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n==1:return 0
        cur_buy_price=prices[0]
        max_profit=0
        profit = 0
        for i in range(1,n):
            if prices[i]<cur_buy_price: # buy when price is less
                cur_buy_price=prices[i]
            else: # sell when price is higher
                profit=prices[i]-cur_buy_price
            max_profit=max(max_profit, profit)
        return max_profit
class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        cur_buy_price = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            profit = max(profit, prices[i]-cur_buy_price)
            cur_buy_price = min(cur_buy_price, prices[i])
        return profit

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        cur_max, max_so_far = 0, 0
        for i in range(1, len(prices)):
            temp = prices[i]-prices[i-1]
            cur_max = max(0, cur_max + prices[i]-prices[i-1])
            max_so_far = max(max_so_far, cur_max)
        return max_so_far