from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        for _ in range(k):
            possible, item_indices = self.canPartitionKSubsetsUtility(nums, k)
            if not possible:
                return False
            for iindex in item_indices:
                nums.pop(iindex)
            k -= 1
        return True

    def canPartitionKSubsetsUtility(self, nums: List[int], k: int):
        if sum(nums) % k:
            return False, []
        n = len(nums)
        SUMM = sum(nums) // k
        numbers = [0]
        for num in nums:
            numbers.append(num)  # converting to 1 based indexing
        dp = [[False] * (SUMM + 1) for _ in range(n + 1)]
        for row in dp:
            row[0] = True
        for i in range(1, n + 1):
            for j in range(1, SUMM + 1):
                item_not_included = dp[i - 1][j]
                if j >= numbers[i] and dp[i - 1][j - numbers[i]]:
                    item_included = True
                else:
                    item_included = False
                if item_included or item_not_included:
                    dp[i][j] = True
        item_indices = []
        if not dp[n][SUMM]:
            return dp[n][SUMM], item_indices
        i, j = n, SUMM
        while i != 0 or j != 0:
            if dp[i][j] == dp[i - 1][j]:
                i -= 1
            else:
                item_indices.append(i - 1)  # item_indices are 0 based
                i, j = i - 1, j - numbers[i]
        return dp[n][SUMM], item_indices
