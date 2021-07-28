import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        max_ending_here=[None]*n # this array could be removed
        max_ending_here[0]=nums[0]
        for i in range(1,n):
            max_ending_here[i]=max(nums[i],max_ending_here[i-1]+nums[i])
        return max(max_ending_here)

class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        max_ending_here=nums[0]
        maxx=nums[0]
        for i in range(1,n):
            max_ending_here=max(nums[i],max_ending_here+nums[i])
            maxx=max(maxx,max_ending_here)
        return maxx
class Solution3:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        cur_sum = 0
        maxx= float('-inf')
        for i in range(n):
            if cur_sum<0: # if negative reset the cur_sum
                cur_sum = nums[i]
            else:
                cur_sum += nums[i] # else add to cur_sum
            maxx = max(maxx, cur_sum)
        return maxx

class Solution4:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        cur_sum = 0
        maxx = float('-inf')
        for i in range(n):
            maxx = max(maxx, nums[i]+cur_sum)
            if cur_sum+nums[i]<0:
                cur_sum =0
            else:
                cur_sum = cur_sum+nums[i]

        return maxx
class Solution5:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx=float('-inf')
        cur_sum=0
        for i in range(len(nums)):
            cur_sum+=nums[i]
            if cur_sum>maxx:
                maxx=cur_sum
            if cur_sum<0: cur_sum=0
        return maxx
class Solution6:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums))

    def get_right_max(self, nums, l, r):
        right_max, temp = float('-inf'), 0
        for i in range(l, r):
            temp += nums[i]
            right_max = max(temp, right_max)
        return right_max

    def get_left_max(self, nums, l, r):
        left_max, temp = float('-inf'), 0
        for i in range(r - 1, l - 1, -1):
            temp += nums[i]
            left_max = max(temp, left_max)
        return left_max

    def helper(self, nums: List[int], l, r) -> int:
        if l == r - 1:
            return nums[l]
        mid = l + (r - l)//2
        max_left = self.get_left_max(nums, l, mid)
        max_right = self.get_right_max(nums, mid, r)
        max_cross = max_left + max_right

        half_left = self.helper(nums, l, mid)
        half_right = self.helper(nums, mid, r)
        return max(half_left, half_right, max_cross)

class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        actual = get_sol().maxSubArray(nums)
        expected = 6
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [-2, -1]
        actual = get_sol().maxSubArray(nums)
        expected = -1
        self.assertEqual(expected, actual)

    def test_3(self):
        nums = [-1]
        actual = get_sol().maxSubArray(nums)
        expected = -1
        self.assertEqual(expected, actual)

    def test_4(self):
        nums = [1]
        actual = get_sol().maxSubArray(nums)
        expected = 1
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        nums = [0]
        actual = solution.maxSubArray(nums)
        expected = 0
        self.assertEqual(expected, actual)

    def test_6(self):
        solution = Solution()
        nums = [-2, -3, -1]
        actual = solution.maxSubArray(nums)
        expected = -1
        self.assertEqual(expected, actual)