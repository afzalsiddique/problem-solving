# https://leetcode.com/problems/product-of-array-except-self/submissions/
# https://leetcode.com/problems/product-of-array-except-self/discuss/65622/Simple-Java-solution-in-O(n)-without-extra-space/67603
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0 for i in range(n)]
        res[0] = 1
        left = 1
        for i in range(1, n):
            left = left * nums[i-1]
            res[i] = left
        right = 1
        for i in range(n-1, 0, -1):
            res[i] = res[i] * right
            right = right * nums[i]
        res[0] = res[0] * right
        return res
