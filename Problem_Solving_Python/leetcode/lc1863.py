import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(start, xor):
            nonlocal res
            res+=xor
            for i in range(start,n):
                dfs(i + 1, xor ^ nums[i])


        n=len(nums)
        res=0
        dfs(0, 0)
        return res

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(6,get_sol().subsetXORSum([1,3]))
    def test2(self):
        self.assertEqual(28,get_sol().subsetXORSum([5,1,6]))
    def test3(self):
        self.assertEqual(480,get_sol().subsetXORSum([3,4,5,6,7,8]))
    def test4(self):
        self.assertEqual(4,get_sol().subsetXORSum([1,1,1]))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
