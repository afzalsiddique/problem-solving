# https://open.kattis.com/problems/magicalcows
from typing import List


#
#
# class Solution:
def count_farms(max_cows, no_farms, no_queries, cows: List[int]):
    MAX_DAYS = 50
    dp = [[0] * (max_cows+1) for _ in range(MAX_DAYS+1)]
    for cow in cows:
        dp[0][cow] += 1
    for row in range(MAX_DAYS):
        for col in range(1, max_cows+1):
            if col * 2 <= max_cows:
                dp[row+1][col * 2] = dp[row][col]
            else:
                dp[row+1][col] += 2 * dp[row][col]
    return dp

print(count_farms(8, 4, 5, [1,3,2,1]))