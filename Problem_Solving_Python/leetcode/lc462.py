import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minMoves2(self, nums):
        n = len (nums)
        mid = n//2
        nums.sort ()
        res = 0
        for i in range (n):
            res = res + abs (nums [i] - nums [mid])
        return res

class tester(unittest.TestCase):
    def test1(self):
        nums = [1,2,3]
        Output = 2
        self.assertEqual(Output,get_sol().minMoves2(nums))
    def test2(self):
        nums = [1,10,2,9]
        Output = 16
        self.assertEqual(Output,get_sol().minMoves2(nums))
    def test3(self):
        nums = [1,0,0,8,6]
        Output = 14
        self.assertEqual(Output,get_sol().minMoves2(nums))
    def test4(self):
        nums = [1,0,0,8,6]
        Output = 14
        self.assertEqual(Output,get_sol().minMoves2(nums))
    def test5(self):
        nums = [1,0,0,8,6]
        Output = 14
        self.assertEqual(Output,get_sol().minMoves2(nums))
