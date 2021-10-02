from itertools import accumulate; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n=len(nums)
        cnt=0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for l in range(k+1,n):
                        if nums[i]+nums[j]+nums[k]==nums[l]:
                            cnt+=1
        return cnt
class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [1,2,3,6]
        Output= 1
        self.assertEqual(Output, get_sol().countQuadruplets(nums))
    def test_2(self):
        nums = [3,3,6,4,5]
        Output= 0
        self.assertEqual(Output, get_sol().countQuadruplets(nums))
    def test_3(self):
        nums = [1,1,1,3,5]
        Output= 4
        self.assertEqual(Output, get_sol().countQuadruplets(nums))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):