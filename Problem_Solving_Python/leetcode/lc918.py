import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass
    def minSubArray(self, nums: List[int]) -> int:
        minn=float('inf')
        cur_sum=0
        for i in range(len(nums)):
            cur_sum+=nums[i]
            if cur_sum<minn:
                minn=cur_sum
            if cur_sum>0: cur_sum=0
        return minn
    def maxSubArray(self, nums: List[int]) -> int:
        maxx=float('-inf')
        cur_sum=0
        for i in range(len(nums)):
            cur_sum+=nums[i]
            if cur_sum>maxx:
                maxx=cur_sum
            if cur_sum<0: cur_sum=0
        return maxx
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # proof
        # max(prefix+suffix)
        # = max(total sum - subarray)
        # = total sum + max(-subarray)
        # = total sum - min(subarray)

        total_sum = sum(nums)
        max_subarray_sum = self.maxSubArray(nums)
        min_subarray_sum = self.minSubArray(nums)
        print(max_subarray_sum,total_sum,min_subarray_sum)
        if min_subarray_sum==total_sum: # if all are negatives at least one element should be selected
            return max_subarray_sum
        return max(max_subarray_sum,total_sum-min_subarray_sum)


class Solution2:
    # https://www.youtube.com/watch?v=Q1TYVUEr-wY
    # time limit
    # time O(n^2)
    # space O(1)
    def maxSubArray(self, nums,start) -> int:
        n=len(nums)
        maxx=float('-inf')
        cur_sum=0
        for i in range(len(nums)):
            cur_sum+=nums[(start+i)%n] # watch out
            if cur_sum>maxx:
                maxx=cur_sum
            if cur_sum<0: cur_sum=0
        return maxx
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=len(nums)
        maxx=float('-inf')
        for i in range(n):
            maxx=max(maxx,self.maxSubArray(nums,i))
        return maxx
class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [1,-2,3,-2]
        Output= 3
        self.assertEqual(Output, get_sol().maxSubarraySumCircular(nums))
    def test_2(self):
        nums = [5,-3,5]
        Output= 10
        self.assertEqual(Output, get_sol().maxSubarraySumCircular(nums))
    def test_3(self):
        nums = [3,-1,2,-1]
        Output= 4
        self.assertEqual(Output, get_sol().maxSubarraySumCircular(nums))
    def test_4(self):
        nums = [3,-2,2,-3]
        Output= 3
        self.assertEqual(Output, get_sol().maxSubarraySumCircular(nums))
    def test_5(self):
        nums = [-2,-3,-1]
        Output= -1
        self.assertEqual(Output, get_sol().maxSubarraySumCircular(nums))
    def test_6(self):
        nums = [2,3,1]
        Output= 6
        self.assertEqual(Output, get_sol().maxSubarraySumCircular(nums))
