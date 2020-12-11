# https://leetcode.com/problems/partition-equal-subset-sum/discuss/90590/Simple-C%2B%2B-4-line-solution-using-a-bitset
# https://leetcode.com/problems/partition-equal-subset-sum/discuss/90590/Simple-C++-4-line-solution-using-a-bitset/94973
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        summ = sum(nums)
        if summ%2:
            return False
        target = summ//2
        dp = [[False]*(target+1) for _ in range(n)]
        if nums[0] <= target: dp[0][nums[0]] = True
        for i in range(n):
            dp[i][0] = True
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                temp = nums[i]
                if j< nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i]]
        return dp[-1][target]


if __name__ == '__main__':
    sol = Solution()
    print(sol.canPartition([6,4,7,5]))
