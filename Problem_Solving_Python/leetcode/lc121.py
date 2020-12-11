# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-%3A)-(In-case-if-interviewer-twists-the-input)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_max, max_so_far = 0, 0
        for i in range(1, len(prices)):
            temp = prices[i]-prices[i-1]
            cur_max = max(0, cur_max + prices[i]-prices[i-1])
            max_so_far = max(max_so_far, cur_max)
        return max_so_far