from typing import List


# two pointers approach
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, 0
        summ = 0
        minn = float('inf')
        while i<n:
            summ += nums[i]
            i+=1
            while summ >= s:
                minn = min(minn, i-j)
                summ -= nums[j]
                j+=1
        return 0 if minn == float('inf') else minn