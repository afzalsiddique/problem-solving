import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=VwylCVAVdmo
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        @functools.lru_cache(None)
        def func(i:int,num_left:int, sum_left:int):
            if num_left==0:
                if not sum_left:
                    return True
                return False
            for j in range(i,n):
                if func(j+1,num_left-1,sum_left-nums[j]):
                    return True
                if func(j+1,num_left,sum_left):
                    return True
            return False

        n=len(nums)
        S=sum(nums)
        for n1 in range(1,n):
            s=S*n1/n
            if math.floor(s)==math.ceil(s): # if it is integer
                if func(0,n1,int(s)):
                    return True
        return False



class Tester(unittest.TestCase):
    def test_1(self):
        self.assertEqual(True,get_sol().splitArraySameAverage(nums = [1,2,3,4,5,6,7,8]))
    def test_2(self):
        self.assertEqual(False,get_sol().splitArraySameAverage(nums = [3,1]))
    def test_3(self):
        self.assertEqual(False,get_sol().splitArraySameAverage(nums = [60,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
