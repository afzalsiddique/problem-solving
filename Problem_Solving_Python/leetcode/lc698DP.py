# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/480707/C%2B%2B-DP-bit-manipulation-in-20-lines
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dp = [-1] * (1 << n)
        dp[0] = 0
        summ = sum(nums)
        if summ % k: return False
        tar = summ//k
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

if __name__ == '__main__':
    sol = Solution()
    nums = [3,7,5]
    k = 3
    print(sol.canPartitionKSubsets(nums, k))