import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # wrong when actual value is used. index should be used
    # case [1,1,1,1,1] fails
    # lis
    def longestArithSeqLength(self, nums):
        dp = {}
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i]-nums[j]
                if (nums[j],diff) in dp:
                    dp[(nums[i],diff)] = dp[(nums[j],diff)] + 1
                else:
                    dp[(nums[i],diff)] = 2
        return max(dp.values())
class Solution2:
    # lis
    def longestArithSeqLength(self, nums):
        dp = {} # (last index, diff)->length
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i]-nums[j]
                if (j,diff) in dp:
                    dp[(i,diff)] = dp[(j,diff)] + 1
                else:
                    dp[(i,diff)] = 2
        return max(dp.values())

class Solution3:
    def longestArithSeqLength(self, nums):
        dp = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff= nums[j] - nums[i]
                if (i,diff) in dp:
                    dp[j, diff] = dp[(i,diff)]+1
                else:
                    dp[j, diff] = 2
        return max(dp.values())

class tester(unittest.TestCase):
    def test01(self):
        nums = [3,6,9,12]
        Output= 4
        self.assertEqual(Output, get_sol().longestArithSeqLength(nums))
    def test02(self):
        nums = [9,4,7,2,10]
        Output= 3
        self.assertEqual(Output, get_sol().longestArithSeqLength(nums))
    def test03(self):
        nums = [20,1,15,3,10,5,8]
        Output= 4
        self.assertEqual(Output, get_sol().longestArithSeqLength(nums))
    def test04(self):
        nums = [12,28,13,6,34,36,53,24,29,2,23,0,22,25,53,34,23,50,35,43,53,11,48,56,44,53,31,6,31,57,46,6,17,42,48,28,5,24,0,14,43,12,21,6,30,37,16,56,19,45,51,10,22,38,39,23,8,29,60,18]
        Output= 4
        self.assertEqual(Output, get_sol().longestArithSeqLength(nums))
    def test05(self):
        nums = [1,1,1,1,1]
        Output= 5
        self.assertEqual(Output, get_sol().longestArithSeqLength(nums))
