import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/patching-array/discuss/78488/Solution-%2B-explanation
    def minPatches(self, nums: List[int], n: int) -> int:
        missing=1
        i=0
        res=0
        # li=[]
        while missing<=n:
            if i<len(nums) and nums[i]<=missing:
                missing+=nums[i]
                i+=1
            else:
                # li.append(missing)
                missing+=missing
                res+=1
        # print(li)
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, get_sol().minPatches( nums = [1, 2, 4, 13, 43],n = 100))
    def test2(self):
        self.assertEqual(9, get_sol().minPatches(nums = [50,200,1000], n = 1100))
    def test3(self):
        self.assertEqual(1, get_sol().minPatches(nums = [1,3], n = 6))
    def test4(self):
        self.assertEqual(2, get_sol().minPatches(nums = [1,5,10], n = 20))
    def test5(self):
        self.assertEqual(0, get_sol().minPatches(nums = [1,2,2], n = 5))
    def test6(self):
        self.assertEqual(0, get_sol().minPatches(nums = [1,2,2,3], n = 8))
    def test7(self):
        self.assertEqual(1, get_sol().minPatches(nums = [1,3,3], n = 8))
    def test8(self):
        self.assertEqual(2, get_sol().minPatches(nums = [1,6,6], n = 15))
