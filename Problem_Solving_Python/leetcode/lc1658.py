import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # time O(n) space O(n)
    # https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/1016199/Python-O(n)-solution-using-cumulative-sums
    # find longest contiguous subarray in the middle
    # return len(nums)-ans
    def minOperations(self, nums, x) :
        n=len(nums)
        nums = [0] + nums # if contiguous sub array starts from the very beginning
        cumsum = list(itertools.accumulate(nums,lambda x,y:x+y))
        di = {c:i for i,c in enumerate(cumsum)}

        goal = cumsum[-1]-x
        if goal<0: return -1
        ans=float('-inf')
        for num in di:
            if num+goal in di:
                ans = max(ans,di[num+goal]-di[num])

        if ans==float('-inf'):
            return -1
        return n-ans
class Solution2:
    # tle
    def minOperations(self, nums: List[int], x: int) -> int:
        dp={}
        def helper(lo,hi,x):
            if (lo,hi) in dp: return dp[lo,hi]
            if x==0: return 0
            if x<0: return float('inf')
            if lo>hi: return float('inf')
            ans= 1+min(helper(lo+1,hi,x-nums[lo]),helper(lo,hi-1,x-nums[hi]))
            dp[lo,hi]=ans
            return ans

        lo=0
        hi=len(nums)-1
        ans=helper(lo,hi,x)
        return ans if ans!=float('inf') else -1


class tester(unittest.TestCase):
    def test_1(self):
        nums = [1,1,4,2,3]
        x = 5
        Output= 2
        self.assertEqual(Output,get_sol().minOperations(nums,x))
    def test_2(self):
        nums = [5,6,7,8,9]
        x = 4
        Output= -1
        self.assertEqual(Output,get_sol().minOperations(nums,x))
    def test_3(self):
        nums = [3,2,20,1,1,3]
        x = 10
        Output= 5
        self.assertEqual(Output,get_sol().minOperations(nums,x))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):