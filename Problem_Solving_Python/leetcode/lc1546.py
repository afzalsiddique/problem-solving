import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

# OVERLAPPING LEETCODE 560
class Solution:
    def maxNonOverlapping(self, A: List[int], k: int) -> int:
        di={}
        di[0]=-1
        res=0
        last=-1
        cur=0
        for i,x in enumerate(A):
            cur+=x
            if cur-k in di and di[cur-k]>=last:
                res+=1
                last=i
            di[cur]=i
        return res
class Solution2:
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
        self.assertEqual(2, get_sol().maxNonOverlapping([3, 5, 1, 4, 2, -9], 6))
    def test02(self):
        self.assertEqual(2, get_sol().maxNonOverlapping([1,1,1,1,1], 2))
    def test03(self):
        self.assertEqual(3,get_sol().maxNonOverlapping([-2,6,6,3,5,4,1,2,8], 10))
    def test04(self):
        self.assertEqual(3,get_sol().maxNonOverlapping([0,0,0], 0))
    def test05(self):
        self.assertEqual(3,get_sol().maxNonOverlapping([1,1,1], 1))
    def test06(self):
        self.assertEqual(2, get_sol().maxNonOverlapping([-1, 3, 5, 1, 4, 2, -9],6))
    def test07(self):
        self.assertEqual(2,get_sol().maxNonOverlapping([-5,5,-4,5,4], 5))
    def test08(self):
        self.assertEqual(0,get_sol().maxNonOverlapping([-5], 5))
