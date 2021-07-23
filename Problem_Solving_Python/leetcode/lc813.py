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
            max_group_size = n-k # divide into exactly k partitions. because it gives the maximum average. otherwise tle
            for i in range(start, max_group_size + 1): # for (int i = s; i + k <= n ; i++)
                left= get_avg(start,i)
                right = h(i+1, k-1)
                ans=max(ans,left+right)
                # l=A[start:i+1]
                # r=A[i+1:]
                # print("{}->{}, {}->{}".format(l,left,r,right))
            dp[start,k]=ans
            return ans
        return h(0,k)

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
    def test_4(self):
        nums = [4663,3020,7789,1627,9668,1356,4207,1133,8765,4649,205,6455,8864,3554,3916,5925,3995,4540,3487,5444,8259,8802,6777,7306,989,4958,2921,8155,4922,2469,6923,776,9777,1796,708,786,3158,7369,8715,2136,2510,3739,6411,7996,6211,8282,4805,236,1489,7698]
        k = 27
        Output= 167436.0833333333
        self.assertEqual(Output,get_sol().largestSumOfAverages(nums,k))
    # def test_5(self):
    # def test_6(self):
