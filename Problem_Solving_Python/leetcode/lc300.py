import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
# https://www.youtube.com/watch?v=1RpMc3fv0y4
# https://www.youtube.com/watch?v=22s1xxRvy28
# https://www.youtube.com/watch?v=TocJOW6vx_I


class Solution:
    ## n log n
    def lengthOfLIS(self, nums):
        sub = []
        for val in nums:
            pos = bisect_left(sub,val)
            if pos == len(sub):
                sub.append(val)

            # elif pos==len(sub)-1: # gives wrong ans
            #     sub[pos] = val
            else:
                sub[pos] = val
        return len(sub)
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp=[1]*n
        for i in range(1, n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[j]+1,dp[i])
        return max(dp)

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(4, get_sol().lengthOfLIS([10,9,2,5,3,7,101,18]))
    def test_2(self):
        self.assertEqual(4, get_sol().lengthOfLIS([0,1,0,3,2,3]))
    def test_3(self):
        self.assertEqual(1, get_sol().lengthOfLIS([7,7,7,7,7,7,7]))
    def test_4(self):
        self.assertEqual(6, get_sol().lengthOfLIS([1,3,6,7,9,4,10,5,6]))
    def test_5(self):
        self.assertEqual(6, get_sol().lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]))
