import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution2()
class Solution:
    def maximumUniqueSubarray(self, A: List[int]) -> int:
        n=len(A)
        l,r=0,0
        di=defaultdict(int)
        maxx=0
        cur=0
        while r<n:
            if di[A[r]]==0:
                di[A[r]]+=1
                cur+=A[r]
                r+=1
                maxx=max(maxx,cur)
            else:
                di[A[l]]-=1
                cur-=A[l]
                l+=1
        return maxx
class Solution2:
    # tle
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        di = {}
        summ, maxx = 0, float('-inf')
        i = 0
        while i!=n:
            if nums[i] not in di:
                di[nums[i]] = i
                summ += nums[i]
                maxx = max(maxx, summ)
                i+=1
            else:
                i = di[nums[i]] + 1
                summ = 0
                di = {}
        return maxx

class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [4,2,4,5,6]
        expected = 17
        self.assertEqual(expected, get_sol().maximumUniqueSubarray(nums))
    def test_2(self):
        nums = [5,2,1,2,5,2,1,2,5]
        expected = 8
        self.assertEqual(expected, get_sol().maximumUniqueSubarray(nums))
    def test_3(self):
        nums = [5,2,1,3]
        expected = 11
        self.assertEqual(expected, get_sol().maximumUniqueSubarray(nums))
    def test_4(self):
        nums = [1,1,1,1,1,1]
        expected = 1
        self.assertEqual(expected, get_sol().maximumUniqueSubarray(nums))
    def test_5(self):
        nums = [1,1,1,2,2,2,2]
        expected = 3
        self.assertEqual(expected, get_sol().maximumUniqueSubarray(nums))
    def test_6(self):
        nums = [1,2,1,2,1,2,1,2]
        expected = 3
        self.assertEqual(expected, get_sol().maximumUniqueSubarray(nums))

