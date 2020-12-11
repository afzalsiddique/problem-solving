from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        dp = {}

        def helper(nums):
            n = len(nums)
            if n == 1: return [nums]
            if tuple(nums) in dp: return dp[tuple(nums)]
            result = []
            for i in range(n):
                new_nums = nums[:i] + nums[i + 1:] # remove ith element
                ans = self.permuteUnique(new_nums)
                for item in ans:
                    if [nums[i]] + item not in result:
                        result.append([nums[i]] + item)
            dp[tuple(nums)] = result
            return result

        return helper(nums)
