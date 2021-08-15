import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        for i in range(0,n-1,2):
            nums[i],nums[i+1]=nums[i+1],nums[i]
        return nums


class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [1,2,3,4,5]
        Output= [1,2,4,5,3]
        self.assertEqual(Output, get_sol().rearrangeArray(nums))
    def test_2(self):
        nums = [0,5,2,1,4]
        Output= 0
        self.assertEqual(Output, get_sol().rearrangeArray(nums))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
