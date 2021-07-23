import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # dp[0] = largest sum which is divisible by 3
    # dp[1] = largest sum when divided by 3, remainder = 1
    # dp[2] = largest sum when divided by 3, remainder = 2
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp=[0,0,0]
        for num in nums:
            dp0,dp1,dp2 = dp[0],dp[1],dp[2] # making a copy for simultaneous update

            tmp=dp0+num
            idx = tmp%3
            dp[idx]=max(dp[idx],tmp)

            tmp=dp1+num
            idx = tmp%3
            dp[idx]=max(dp[idx],tmp)

            tmp=dp2+num
            idx = tmp%3
            dp[idx]=max(dp[idx],tmp)
        return dp[0]
class Solution2:
    # dp[0] = largest sum which is divisible by 3
    # dp[1] = largest sum when divided by 3, remainder = 1
    # dp[2] = largest sum when divided by 3, remainder = 2
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp=[0,0,0]
        for num in nums:
            for tmp in dp[:]:# making a copy for simultaneous update
                dp[(tmp+num)%3]=max(dp[(tmp+num)%3],tmp+num)
        return dp[0]

class tester(unittest.TestCase):
    def test_1(self):
        nums = [3,6,5,1,8]
        Output= 18
        self.assertEqual(Output, get_sol().maxSumDivThree(nums))
    def test_2(self):
        nums = [4]
        Output= 0
        self.assertEqual(Output, get_sol().maxSumDivThree(nums))
    def test_3(self):
        nums = [1,2,3,4,4]
        Output= 12
        self.assertEqual(Output, get_sol().maxSumDivThree(nums))
    def test_4(self):
        nums = [2,6,2,2,7]
        Output= 15
        self.assertEqual(Output, get_sol().maxSumDivThree(nums))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
