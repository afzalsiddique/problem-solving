# https://leetcode.com/problems/jump-game/
# https://www.youtube.com/watch?v=cETfFsSTGJI
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n==1:
            return True
        dp = [float('inf')]*n
        dp[0] = 0
        for i in range(1, n):
            for j in range(0, i):
                if j+ nums[j]>=i:
                    dp[i] = min(dp[i], dp[j]+1)
        if dp[n-1]==float('inf'):
            return False
        return True