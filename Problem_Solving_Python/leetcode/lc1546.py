import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

# OVERLAPPING LEETCODE 560
class Solution:
    # https://www.youtube.com/watch?v=0LWRSbYH5oM
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

class MyTestCase(unittest.TestCase):
    def test01(self):
        nums = [-1, 3, 5, 1, 4, 2, -9]
        target = 6
        Output=2
        self.assertEqual(Output, get_sol().maxNonOverlapping(nums, target))
    def test02(self):
        nums = [1,1,1,1,1]
        target = 2
        Output = 2
        self.assertEqual(Output, get_sol().maxNonOverlapping(nums, target))
    def test03(self):
        nums,target = [-2,6,6,3,5,4,1,2,8], 10
        Output= 3
        self.assertEqual(Output,get_sol().maxNonOverlapping(nums,target))
    def test04(self):
        nums,target = [0,0,0], 0
        Output= 3
        self.assertEqual(Output,get_sol().maxNonOverlapping(nums,target))
    def test05(self):
        nums,target = [1,1,1], 1
        Output= 3
        self.assertEqual(Output,get_sol().maxNonOverlapping(nums,target))
