from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        n = len(nums)
        SUMM = sum(nums) // 2
        numbers = [0]
        for num in nums:
            numbers.append(num) # converting to 1 based indexing
        dp = [[False]*(SUMM+1) for _ in range(n+1)]
        for row in dp:
            row[0] = True
        for i in range(1, n+1):
            for j in range(1, SUMM+1):
                item_not_included = dp[i-1][j]
                if j >= numbers[i] and dp[i-1][j-numbers[i]]:
                    item_included = True
                else:
                    item_included = False
                if item_included or item_not_included:
                    dp[i][j] = True
        return dp[n][SUMM]