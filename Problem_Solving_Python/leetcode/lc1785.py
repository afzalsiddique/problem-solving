import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        summ=sum(nums)
        left=goal-summ
        return math.ceil(abs(left)/limit)

class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums,limit,goal = [1,-1,1],3,-4
        Output= 2
        self.assertEqual(Output, get_sol().minElements(nums,limit,goal))
    def test_2(self):
        nums,limit,goal = [1,-10,9,1],100,0
        Output= 1
        self.assertEqual(Output, get_sol().minElements(nums,limit,goal))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):