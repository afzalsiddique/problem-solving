from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0

        dp = [0] * n
        min_price = prices[0]
        for i in range(n):
            a = dp[i-1]
            b = prices[i]-min_price
            dp[i] = max(dp[i - 1], prices[i] - min_price)
            min_price = min(min_price, prices[i] - min_price)
        return dp[-1]