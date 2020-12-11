# https://leetcode.com/problems/partition-equal-subset-sum/discuss/90590/Simple-C%2B%2B-4-line-solution-using-a-bitset
# https://leetcode.com/problems/partition-equal-subset-sum/discuss/90590/Simple-C++-4-line-solution-using-a-bitset/94973

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_val = sum(nums)
        if sum_val % 2 == 1:
            return False
        target = sum_val // 2
        dp = [False] * (sum_val + 1)
        dp[0] = True
        for i in range(len(nums)):
            next_dp = [False] * (sum_val + 1)
            for j in range(len(dp)):
                if dp[j]:
                    next_dp[j + nums[i]] = True
                    next_dp[j] = True
            dp = next_dp
        return dp[target]


if __name__ == '__main__':
    sol = Solution()
    print(sol.canPartition([6, 4, 7, 5]))
