import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def max_sub_sum(self,A):
        n=len(A)
        max_ending_here=[float('-inf')]*n
        max_ending_here[0]=max(0,A[0])
        for i in range(1,n):
            max_ending_here[i]=max(max_ending_here[i-1]+A[i],A[i])
        return max(max_ending_here)
    def min_sub_sum(self,A):
        n=len(A)
        min_ending_here=[float('inf')]*n
        min_ending_here[0]=min(0,A[0])
        for i in range(1,n):
            min_ending_here[i]=min(min_ending_here[i-1]+A[i],A[i])
        return min(min_ending_here)
    def maxAbsoluteSum(self, A: List[int]) -> int:
        maxx=self.max_sub_sum(A)
        minn=self.min_sub_sum(A)
        return max(maxx,abs(minn))
class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [1,-3,2,3,-4]
        Output= 5
        self.assertEqual(Output, get_sol().maxAbsoluteSum(nums))
    def test_2(self):
        nums = [2,-5,1,-4,3,-2]
        Output= 8
        self.assertEqual(Output, get_sol().maxAbsoluteSum(nums))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
