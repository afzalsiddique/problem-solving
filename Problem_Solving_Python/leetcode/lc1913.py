import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        first_max=max(nums)
        nums.remove(first_max)
        second_max=max(nums)
        nums.remove(second_max)
        first_min=min(nums)
        nums.remove(first_min)
        second_min=min(nums)
        nums.remove(second_min)
        return (first_max*second_max)-(first_min*second_min)




class tester(unittest.TestCase):
    def test01(self):
        nums = [5,6,2,7,4]
        Output= 34
        self.assertEqual(Output,get_sol().maxProductDifference(nums))
    def test02(self):
        nums = [4,2,5,9,7,4,8]
        Output= 64
        self.assertEqual(Output,get_sol().maxProductDifference(nums))
    # def test03(self):