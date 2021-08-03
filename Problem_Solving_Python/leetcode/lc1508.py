import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/discuss/730511/C++-priority_queue-solution/728004
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        left-=1 # 0 based index
        right-=1 # 0 based index
        pq=[(nums[i],i+1) for i in range(n)]
        heapify(pq)
        ans=0
        for i in range(right+1):
            cur_num,j=heappop(pq) # elements are coming out in sorted order
            if i>=left:
                ans+=cur_num
                ans%=10**9+7
            if j<n:
                heappush(pq,(cur_num+nums[j],j+1))
        return ans
class Tester(unittest.TestCase):
    def test_1(self):
        nums,n,left,right = [1,2,3,4],4,1,5
        Output= 13
        self.assertEqual(Output,get_sol().rangeSum(nums,n,left,right))
    def test_2(self):
        nums,n,left,right = [1,2,3,4],4,3,4
        Output= 6
        self.assertEqual(Output,get_sol().rangeSum(nums,n,left,right))
    def test_3(self):
        nums,n,left,right = [1,2,3,4],4,1,10
        Output= 50
        self.assertEqual(Output,get_sol().rangeSum(nums,n,left,right))
    # def test_4(self):
