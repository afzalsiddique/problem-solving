import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution1:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for i in range(n-1):
            j = i + 1
            dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        for i in range(n-3, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = max(dp[i][j-1], dp[i][j-2] + nums[j])
        return dp[0][-1]
class Solution2:
    # recursive dp
    # right to left
    # time O(n) space O(n)
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)
        def helper(i):
            if i<0: return 0
            if dp[i]!=-1: return dp[i]
            take_it = nums[i]+helper(i-2)
            leave_it = helper(i-1)
            dp[i]=max(take_it,leave_it)
            return dp[i]

        return helper(len(nums)-1)
class Solution3:
    # recursive dp
    # left to right
    # time O(n) space O(n)
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        def helper(i):
            if i>=n: return 0
            if dp[i]!=-1: return dp[i]
            take_it = nums[i]+helper(i+2)
            leave_it = helper(i+1)
            dp[i]=max(take_it,leave_it)
            return dp[i]

        return helper(0)
class Solution4:
    # iterative dp
    # time O(n) space O(n)
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1: return nums[0]
        dp = [-1]*n
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n):
            dp[i]=max(dp[i-1],nums[i]+dp[i-2])
        return max(dp[-1],dp[-2])
class Solution:
    # iterative
    # time O(n) space O(1)
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1: return nums[0]
        second_last=nums[0]
        last=max(nums[0],nums[1])
        for i in range(2,n):
            cur=max(last,nums[i]+second_last)
            second_last=last
            last=cur
        return max(last,second_last)



class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(4,get_sol().rob([1,2,3,1]))
    def test02(self):
        self.assertEqual(12,get_sol().rob([2,7,9,3,1]))
    def test03(self):
        self.assertEqual(2,get_sol().rob([2,1]))
    def test04(self):
        self.assertEqual(3365,get_sol().rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]))
    def test05(self):
        self.assertEqual(4,get_sol().rob([2,1,1,2]))
    def test06(self):
        self.assertEqual(2,get_sol().rob([1,2]))
