# https://leetcode.com/problems/maximum-product-subarray/
# https://leetcode.com/problems/maximum-product-subarray/discuss/847520/Thought-process-and-useful-strategy
# https://www.youtube.com/watch?v=hJ_Uy2DzE08

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx = [nums[0]]
        minn = [nums[0]]
        for i in range(1, len(nums)):
            maxx.append(max(nums[i], nums[i]*maxx[i-1], nums[i]*minn[i-1]))
            minn.append(min(nums[i], nums[i]*maxx[i-1], nums[i]*minn[i-1]))
        return max(maxx)