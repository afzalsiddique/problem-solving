# https://leetcode.com/problems/jump-game/
# https://www.youtube.com/watch?v=cETfFsSTGJI
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n==1:
            return True
        reach = 0
        i = 0
        while(i<=reach and i<n):
            reach = max(reach, i+nums[i])
            i+=1
        if reach>=n-1:
            return True
        return False