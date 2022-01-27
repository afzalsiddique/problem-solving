from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *
def get_sol(): return Solution()
# https://leetcode.com/problems/partition-equal-subset-sum/discuss/90590/Simple-C%2B%2B-4-line-solution-using-a-bitset
# https://leetcode.com/problems/partition-equal-subset-sum/discuss/90590/Simple-C++-4-line-solution-using-a-bitset/94973
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def recur(i, cur):
            if cur==target:
                return True
            if i==n:
                return False
            if cur>target:
                return False
            if recur(i+1,cur+nums[i]): # pick ith number
                return True
            return recur(i+1,cur) # do not pick ith number

        n=len(nums)
        summ=sum(nums)
        if summ%2: return False
        target=summ//2
        return recur(0,0)
class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        n = len(nums)
        target = sum(nums) // 2
        nums=[0]+nums # add dummy
        dp = [[False]*(target+1) for _ in range(n+1)]
        for row in dp:
            row[0] = True
        for i in range(1, n+1):
            for j in range(1, target+1):
                item_not_included = dp[i-1][j]
                if j >= nums[i] and dp[i-1][j-nums[i]]:
                    item_included = True
                else:
                    item_included = False
                if item_included or item_not_included:
                    dp[i][j] = True
        return dp[n][target]
class Solution6:
    # https://leetcode.com/problems/partition-equal-subset-sum/discuss/90590/Simple-C%2B%2B-4-line-solution-using-a-bitset
    # https://leetcode.com/problems/partition-equal-subset-sum/discuss/90590/Simple-C++-4-line-solution-using-a-bitset/94973
    def canPartition(self, nums:List[int])->int:
        sum_val = 0
        bits = 1
        bin_bits = bin(bits)
        for num in nums:
            sum_val += num
            temp = bits << num
            bin_temp = bin(temp)
            bits |= temp
            bin_bits = bin(bits)

        return (not sum_val % 2 == 1) and (bits >> (sum_val // 2)) & 1 == 1
class Solution8:
    # solution will work
    #     1. if nums.length <= 16
    #     2. sum(nums) is large
    def canPartition(self, nums):
        n = len(nums)
        dp = [-1] * (1 << n)
        dp[0] = 0
        summ = sum(nums)
        if summ % 2: return False
        tar = summ//2
        for mask in range(1<<n):
            if dp[mask] == -1: # states that were not calculated because sum of included items crosses the target
                continue
            for i in range(n):
                selected = bin(mask&(1<<i))
                total = dp[mask]+nums[i]
                if not (mask&(1<<i)) and dp[mask]+nums[i] <= tar:
                    temp_idx = mask|(1<<i)
                    temp = (dp[mask]+nums[i]) % tar
                    dp[mask|(1<<i)] = (dp[mask]+nums[i]) % tar

        return dp[(1<<n)-1] == 0
class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, get_sol().canPartition([5,4,2,2,4,3]))
    def test2(self):
        self.assertEqual(True, get_sol().canPartition([1, 5, 11, 5]))
    def test3(self):
        self.assertEqual(False, get_sol().canPartition([1, 2, 3, 5]))
    def test4(self):
        self.assertEqual(True, Solution().canPartition([6,4,7,5]))
    def test5(self):
        self.assertEqual(True, get_sol().canPartition([1, 1]))
    def test6(self):
        self.assertEqual(False, get_sol().canPartition([1,2,5]))
    def test7(self):
        self.assertEqual(False, get_sol().canPartition([2,2,3,5]))
    def test8(self):
        self.assertEqual(False, get_sol().canPartition([100]))
