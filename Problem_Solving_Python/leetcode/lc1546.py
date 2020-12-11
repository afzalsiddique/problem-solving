# https://www.youtube.com/watch?v=0LWRSbYH5oM
from typing import List


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefix_sum = 0
        res = 0
        di = {0:-1}
        prev_index = -1
        for i in range(len(nums)):
            prefix_sum += nums[i]
            remain = prefix_sum - target
            if remain in di and di[remain] >= prev_index:
                prev_index = i
                res+=1
            di[prefix_sum] = i
        return res