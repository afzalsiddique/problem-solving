from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def rob(self, A: List[int]) -> int:
        @cache
        def dp(i,canRobThisHouse,last):
            if i==last:
                return 0
            if canRobThisHouse:
                return max(A[i]+dp(i+1,False,last),dp(i+1,True,last))
            return dp(i+1,True,last)

        n=len(A)
        if n==1: return A[0]
        return max(dp(0,True,n-1),dp(0,False,n))
class Solution2:
    # https://leetcode.com/problems/house-robber-ii/discuss/59934/Simple-AC-solution-in-Java-in-O(n)-with-explanation/61023
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            n = len(nums)
            prev_yes, prev_no = 0, 0
            for i in range(n):
                prev_yes, prev_no = max(prev_yes, prev_no), nums[i] + prev_yes
            return max(prev_yes, prev_no)

        n = len(nums)
        if n <= 3: return max(nums)
        return max(helper(nums[1:]), nums[0] + helper(nums[2:-1]))
class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(3,get_sol().rob( [2,3,2]))
    def test02(self):
        self.assertEqual(4,get_sol().rob([1,2,3,1]))
    def test03(self):
        self.assertEqual(3,get_sol().rob([1,2,3]))
    def test04(self):
        self.assertEqual(1,get_sol().rob([1]))
    def test05(self):
        self.assertEqual(2,get_sol().rob([2,1]))
    # def test06(self):
