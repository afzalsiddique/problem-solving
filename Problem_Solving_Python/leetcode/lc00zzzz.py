import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxSubArray(self, A: List[int]) -> int:
        n=len(A)
        max_ending_here=[float('-inf')]*n
        max_ending_here[0]=A[0]
        for i in range(1,n):
            max_ending_here[i]=max(max_ending_here[i-1]+A[i],A[i])
        return max(max_ending_here)

class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        actual = get_sol().maxSubArray(nums)
        expected = 6
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [-2, -1]
        actual = get_sol().maxSubArray(nums)
        expected = -1
        self.assertEqual(expected, actual)

    def test_3(self):
        nums = [-1]
        actual = get_sol().maxSubArray(nums)
        expected = -1
        self.assertEqual(expected, actual)

    def test_4(self):
        nums = [1]
        actual = get_sol().maxSubArray(nums)
        expected = 1
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        nums = [0]
        actual = solution.maxSubArray(nums)
        expected = 0
        self.assertEqual(expected, actual)

    def test_6(self):
        solution = Solution()
        nums = [-2, -3, -1]
        actual = solution.maxSubArray(nums)
        expected = -1
        self.assertEqual(expected, actual)
