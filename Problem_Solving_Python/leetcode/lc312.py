import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @functools.lru_cache(None)
        def search(nums:tuple[int]):
            ans=0
            for i in range(1,len(nums)-1):
                part1=search(nums[:i+1]) # if we are bursting ith balloon at the very last, then this will be part of left recursive call. That's why "i+1"
                part2=nums[0]*nums[i]*nums[-1]
                part3=search(nums[i:]) # i will be part of right recursive call
                ans=max(ans,part1+part2+part3)
            return ans

        nums=tuple([1]+nums+[1])
        return search(nums)
class Solution2:
    # tle
    def maxCoins(self, nums: List[int]) -> int:
        @functools.lru_cache(None)
        def search(left,right):
            ans=0
            for i in range(left+1,right):
                part1=search(left,i) # if we are bursting ith balloon at the very last, then this will be part of left recursive call.
                part2=nums[left]*nums[i]*nums[right]
                part3=search(i,right) # i will be part of right recursive call
                ans=max(ans,part1+part2+part3)
            return ans

        nums=[1]+nums+[1]
        return search(0,len(nums)-1) # both inclusive
class Solution3:
    # https://www.youtube.com/watch?v=uG_MtaCJIrM
    def maxCoins(self, nums):
        nums = [1] + nums + [1]  # build the complete array
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for window in range(1, n):
            for left in range(n - window):
                right = left + window
                for k in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right])
        return dp[0][n - 1]


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(167, get_sol().maxCoins([3,1,5,8]))
    def test_2(self):
        self.assertEqual(152, get_sol().maxCoins([3,5,8]))
    def test_3(self):
        self.assertEqual(48, get_sol().maxCoins([5,8]))
    def test_4(self):
        self.assertEqual(20, get_sol().maxCoins([3,5]))
    def test_5(self):
        self.assertEqual(0, get_sol().maxCoins([]))
    def test_6(self):
        self.assertEqual(1654, get_sol().maxCoins([7,9,8,0,7,1,3,5,5,2,3]))
    def test_7(self):
        self.assertEqual(48, get_sol().maxCoins([5,8]))
    def test_8(self):
        self.assertEqual(498010100, get_sol().maxCoins([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]))