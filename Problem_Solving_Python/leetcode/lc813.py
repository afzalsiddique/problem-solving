import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # check lc813.bmp for recursion tree
    # https://leetcode.com/problems/largest-sum-of-averages/discuss/126280/Naive-Detailed-Step-by-Step-Approach-from-Recursive-to-DP-O(N)-solution
    def largestSumOfAverages(self, A: List[int], k: int) -> float:
        def get_avg(lo,hi): return (cumsum[hi]-cumsum[lo]+A[lo])/(hi-lo+1)
        n=len(A)
        cumsum=list(itertools.accumulate(A))
        dp={}
        def h(start,k):
            if (start,k) in dp: return dp[start,k]
            if k==1: return get_avg(start, n - 1)
            ans = 0
            for i in range(start, n - k + 1):
                left= get_avg(start,i)
                right = h(i+1, k-1)
                ans=max(ans,left+right)
            dp[start,k]=ans
            return ans
        return h(0,k)
class Solution2:
    # only for visualization
    def largestSumOfAverages(self, A: List[int], k: int) -> float:
        def h(nums,k):
            cumsum=list(itertools.accumulate(nums))
            hi=len(nums)-1
            lo=0
            if k==1: return (cumsum[hi]-cumsum[lo]+nums[lo])/(hi-lo+1)
            ans = float('-inf')
            for i in range(len(nums)-k+1):
                left=(cumsum[i] - cumsum[lo] + nums[lo]) / (i - lo + 1)
                right = h(nums[i+1:],k-1)
                ans =max(ans,left+right)
            print("{}->{}".format(nums,ans))
            return ans

        return h(A,k)

class tester(unittest.TestCase):
    def test_1(self):
        nums = [9,1,2,3,9]
        k = 2
        Output= 12.75
        self.assertEqual(Output,get_sol().largestSumOfAverages(nums,k))
    def test_2(self):
        nums = [9,1,2,3,9]
        k = 3
        Output= 20
        self.assertEqual(Output,get_sol().largestSumOfAverages(nums,k))
    def test_3(self):
        nums = [1,2,3,4,5,6,7]
        k = 4
        Output= 20.5
        self.assertEqual(Output,get_sol().largestSumOfAverages(nums,k))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
