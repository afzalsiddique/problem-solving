import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9+7
        n=len(nums)
        li = [0]*(n+1)
        for start,end in requests:
            li[start]+=1
            li[end+1]-=1
        freq = list(itertools.accumulate(li))
        freq = [[x,i] for i,x in enumerate(freq)]
        freq.sort(reverse=True)
        nums.sort(reverse=True)
        for i in range(n):
            freq[i][0]=nums[i]
        freq.sort(key=lambda x:(x[1]))
        perm = [x[0] for x in freq]
        pre_sum = list(itertools.accumulate(perm))
        ans=0
        for start,end in requests:
            ans += pre_sum[end]-pre_sum[start]+perm[start]
            ans %= MOD
        return ans

class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums,requests,Output = [1,2,3,4,5], [[1,3],[0,1]],19
        self.assertEqual(Output, get_sol().maxSumRangeQuery(nums,requests))
    def test_2(self):
        nums,requests,Output = [1,2,3,4,5,6], [[0,1]],11
        self.assertEqual(Output, get_sol().maxSumRangeQuery(nums,requests))
    def test_3(self):
        nums,requests,Output = [1,2,3,4,5,10], [[0,2],[1,3],[1,1]],47
        self.assertEqual(Output, get_sol().maxSumRangeQuery(nums,requests))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
