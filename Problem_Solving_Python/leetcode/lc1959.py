import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # We split the nums array to k + 1 intervals. The array size does not change within that invernal, so that the size of the array for each interval is the largest element in that interval.
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        def f(i,k):
            if i==n: return 0
            if k==n-i: return 0
            if k==-1: return float('inf')
            if (i,k) in dp: return dp[i,k]
            ans = float('inf')
            cur_sum = 0
            maxx=0
            for j in range(i,n):
                maxx=max(maxx,nums[j])
                cur_sum+=nums[j]
                wasted = maxx*(j-i+1)- cur_sum
                ans = min(ans,wasted+f(j+1,k-1))
            dp[i,k]=ans
            return ans

        n=len(nums)
        dp = {}
        return f(0,k)


class MyTestCase(unittest.TestCase):
    def test1(self):
        nums,k = [10,20,30],  1
        Output= 10
        self.assertEqual(Output, get_sol().minSpaceWastedKResizing(nums,k))
    def test2(self):
        nums,k = [10,20],  0
        Output= 10
        self.assertEqual(Output, get_sol().minSpaceWastedKResizing(nums,k))
    def test3(self):
        nums,k = [10,20,15,30,20],  2
        Output= 15
        self.assertEqual(Output, get_sol().minSpaceWastedKResizing(nums,k))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
