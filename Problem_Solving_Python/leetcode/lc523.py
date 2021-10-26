import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        di = defaultdict(lambda :float('inf'))
        di[0]=-1
        cur = 0
        for i in range(len(nums)):
            cur = (cur + nums[i])%k
            prev_idx = di[cur]
            if i-prev_idx>=2: return True
            if cur not in di or di[cur]==float('inf'):
                di[cur]=i
        return False

class MyTestCase(unittest.TestCase):
    def test1(self):
        nums,k = [23,2,4,6,7],  6
        Output= True
        self.assertEqual(Output, get_sol().checkSubarraySum(nums,k))
    def test2(self):
        nums,k = [23,2,6,4,7],  6
        Output= True
        self.assertEqual(Output, get_sol().checkSubarraySum(nums,k))
    def test3(self):
        nums,k = [23,2,6,4,7],  13
        Output= False
        self.assertEqual(Output, get_sol().checkSubarraySum(nums,k))
    def test4(self):
        nums,k = [23,2,4,6,6], 7
        Output= True
        self.assertEqual(Output, get_sol().checkSubarraySum(nums,k))
    def test5(self):
        nums,k = [0], 1
        Output= False
        self.assertEqual(Output, get_sol().checkSubarraySum(nums,k))
    def test6(self):
        nums,k = [5,0,0,0], 3
        Output= True
        self.assertEqual(Output, get_sol().checkSubarraySum(nums,k))
    def test7(self):
        nums,k = [0,0], 1
        Output= True
        self.assertEqual(Output, get_sol().checkSubarraySum(nums,k))
    def test8(self):
        nums,k = [1,0], 2
        Output= False
        self.assertEqual(Output, get_sol().checkSubarraySum(nums,k))
    def test9(self):
        nums,k = [7,0], 7
        Output= True
        self.assertEqual(Output, get_sol().checkSubarraySum(nums,k))
    def test10(self):
        nums,k = [7], 7
        Output= False
        self.assertEqual(Output, get_sol().checkSubarraySum(nums,k))
    def test11(self):
        nums,k = [1,2,0], 6
        Output= False
        self.assertEqual(Output, get_sol().checkSubarraySum(nums,k))
    def test12(self):
        nums,k = [2,4,3], 6
        Output= True
        self.assertEqual(Output, get_sol().checkSubarraySum(nums,k))
    def test13(self):
        nums,k = [1,1], 1
        Output= True
        self.assertEqual(Output, get_sol().checkSubarraySum(nums,k))
    def test14(self):
        nums,k = [1,0,1,0,1], 4
        Output= False
        self.assertEqual(Output, get_sol().checkSubarraySum(nums,k))
    def test15(self):
        nums,k = [5,2,0,2,5], 6
        Output= False
        self.assertEqual(Output, get_sol().checkSubarraySum(nums,k))
    def test16(self):
        nums,k = [1,2,3], 5
        Output= True
        self.assertEqual(Output, get_sol().checkSubarraySum(nums,k))
