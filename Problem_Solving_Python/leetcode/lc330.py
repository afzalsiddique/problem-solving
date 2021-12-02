import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/patching-array/discuss/78488/Solution-%2B-explanation
    def minPatches(self, nums: List[int], n: int) -> int:
        missing=1
        i=0
        res=0
        li=[]
        while missing<=n:
            if i<len(nums) and nums[i]<=missing:
                missing+=nums[i]
                i+=1
            else:
                li.append(missing)
                missing+=missing
                res+=1
        # print(li)
        return res

class MyTestCase(unittest.TestCase):
    def test01(self):
        actual = get_sol().minPatches( nums = [1, 2, 4, 13, 43],n = 100)
        Output= 2
        self.assertEqual(Output, actual)
    def test1(self):
        actual = get_sol().minPatches(nums = [50,200,1000], n = 1100)
        Output= 9
        self.assertEqual(Output, actual)
    def test2(self):
        actual = get_sol().minPatches(nums = [1,3], n = 6)
        Output= 1
        self.assertEqual(Output, actual)
    def test3(self):
        actual = get_sol().minPatches(nums = [1,5,10], n = 20)
        Output= 2
        self.assertEqual(Output, actual)
    def test4(self):
        actual = get_sol().minPatches(nums = [1,2,2], n = 5)
        Output= 0
        self.assertEqual(Output, actual)
    def test5(self):
        actual = get_sol().minPatches(nums = [1,2,2,3], n = 8)
        Output= 0
        self.assertEqual(Output, actual)
