# solution will work
#     1. if nums.length <= 16
#     2. sum(nums) is large
class Solution:
    def canPartition(self, nums):
        n = len(nums)
        dp = [-1] * (1 << n)
        dp[0] = 0
        summ = sum(nums)
        if summ % 2: return False
        tar = summ//2
        for mask in range(1<<n):
            if dp[mask] == -1: # states that were not calculated because sum of included items crosses the target
                continue
            for i in range(n):
                selected = bin(mask&(1<<i))
                total = dp[mask]+nums[i]
                if not (mask&(1<<i)) and dp[mask]+nums[i] <= tar:
                    temp_idx = mask|(1<<i)
                    temp = (dp[mask]+nums[i]) % tar
                    dp[mask|(1<<i)] = (dp[mask]+nums[i]) % tar

        return dp[(1<<n)-1] == 0
