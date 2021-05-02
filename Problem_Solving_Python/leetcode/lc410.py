import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
# https://leetcode.com/problems/split-array-largest-sum/discuss/89846/Python-solution-with-detailed-explanation
class Solution:
    def is_valid(self, nums, m, mid):
        # assume mid is < max(nums)
        cuts, curr_sum  = 0, 0
        for x in nums:
            curr_sum += x
            if curr_sum > mid:
                cuts, curr_sum = cuts+1, x
        subs = cuts + 1
        return (subs <= m)

    def splitArray(self, nums, m):
        low, high, ans = max(nums), sum(nums), -1
        while low <= high:
            mid = (low+high)//2
            if self.is_valid(nums, m, mid): # can you make at-most m sub-arrays with maximum sum atmost mid
                ans, high = mid, mid-1
            else:
                low = mid + 1
        return ans
class tester(unittest.TestCase):
    def test1(self):
        nums = [7,2,5,10,8]
        m = 2
        Output= 18
        self.assertEqual(Output,Solution().splitArray(nums,m))