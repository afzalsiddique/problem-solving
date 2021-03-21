# https://www.youtube.com/watch?v=MiqoA-yF-0M
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List


class Solution:
    def maxAscendingSum(self,nums: List[int]) -> int:
        n = len(nums)
        maxx = float('-inf')
        for i in range(n):
            summ = nums[i]
            for j in range(i+1,n):
                if nums[j]>nums[j-1]:
                    summ+=nums[j]
                else:
                    break
            maxx=max(maxx, summ)
        return maxx

