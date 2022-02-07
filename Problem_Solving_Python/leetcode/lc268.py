import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution2()
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        for i in range(n):
            res^=i
        res^=n
        for x in nums:
            res^=x
        return res

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        res=(n*(n+1))//2
        for x in nums:
            res-=x
        return res


class tester(unittest.TestCase):
    def test1(self):
        Output= 2
        self.assertEqual(Output,get_sol().missingNumber(nums = [3,0,1]))
    def test2(self):
        Output= 2
        self.assertEqual(Output,get_sol().missingNumber(nums = [0,1]))
    def test3(self):
        Output= 8
        self.assertEqual(Output,get_sol().missingNumber(nums = [9,6,4,2,3,5,7,0,1]))
    def test4(self):
        Output= 1
        self.assertEqual(Output,get_sol().missingNumber(nums = [0]))