import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        # print(n)
        i=nums.index(min(nums))
        j=nums.index(max(nums))
        # print(i,j)

        if min(n-j,j+1)<min(n-i,i+1): # make i is closer to boundary
            i,j=j,i
        # print(i,j)
        if i<j: # i is closer to left boundary
            return min(n-j+i+1,j+1,n-i)
        return min(n-i+j+1,i+1,n-j) # i is closer to right boundary

class MyTestCase(unittest.TestCase):
    def test1(self):
        nums = [2,10,7,5,4,1,8,6]
        Output= 5
        self.assertEqual(Output, get_sol().minimumDeletions(nums))
    def test2(self):
        nums = [0,-4,19,1,8,-2,-3,5]
        Output= 3
        self.assertEqual(Output, get_sol().minimumDeletions(nums))
    def test3(self):
        nums = [101]
        Output= 1
        self.assertEqual(Output, get_sol().minimumDeletions(nums))
    def test4(self):
        nums = [41,-47,-26,57,82,-23,47,52,42,79,2,77,0,-4,1,-99,-57,72,-95]
        Output= 9
        self.assertEqual(Output, get_sol().minimumDeletions(nums))
    def test5(self):
        nums = [-14,61,29,-18,59,13,-67,-16,55,-57,7,74]
        Output= 6
        self.assertEqual(Output, get_sol().minimumDeletions(nums))
    # def test6(self):
    # def test7(self):
    # def test8(self):
