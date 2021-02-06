from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        di = {}
        summ, maxx = 0, float('-inf')
        i = 0
        while i!=n:
            if nums[i] not in di:
                di[nums[i]] = i
                summ += nums[i]
                maxx = max(maxx, summ)
                i+=1
            else:
                temp = di[nums[i]] + 1
                di.pop(nums[i])
                i = temp
                summ = 0
                di = {}
        return maxx