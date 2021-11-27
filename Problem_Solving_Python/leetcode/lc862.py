import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/189039/Detailed-intuition-behind-Deque-solution
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        res=float('inf')
        deq = deque()
        pre = [0]+list(itertools.accumulate(nums))
        for i in range(n+1):
            while deq and pre[i]-pre[deq[0]]>=k:
                res=min(res,i-deq.popleft())
            while deq and pre[i]<=pre[deq[-1]]:
                deq.pop()
            deq.append(i)
        return -1 if res==float('inf') else res



class MyTestCase(unittest.TestCase):
    def test1(self):
        nums,k = [1],  1
        Output= 1
        self.assertEqual(Output, get_sol().shortestSubarray(nums,k))
    def test2(self):
        nums,k = [1,2],  4
        Output= -1
        self.assertEqual(Output, get_sol().shortestSubarray(nums,k))
    def test3(self):
        nums,k = [2,-1,2],  3
        Output= 3
        self.assertEqual(Output, get_sol().shortestSubarray(nums,k))
    def test4(self):
        nums,k = [56,-21,56,35,-9], 61
        Output= 2
        self.assertEqual(Output, get_sol().shortestSubarray(nums,k))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
