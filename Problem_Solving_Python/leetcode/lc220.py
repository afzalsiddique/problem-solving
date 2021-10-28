import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        w = t+1 # width of window
        di = {}
        for i,num in enumerate(nums):
            num = nums[i]
            bucket_no = num//w
            if bucket_no in di:
                return True
            if bucket_no-1 in di and abs(di[bucket_no-1]-num)<=t:
                return True
            if bucket_no+1 in di and abs(di[bucket_no+1]-num)<=t:
                return True
            di[bucket_no]=num
            if i>=k:
                prev = nums[i-k]
                prev_bucket_no = prev//w
                di.pop(prev_bucket_no,None)
        return False


class MyTestCase(unittest.TestCase):
    def test1(self):
        nums,k,t = [1,2,3,1],  3, 0
        Output= True
        self.assertEqual(Output, get_sol().containsNearbyAlmostDuplicate(nums,k,t))
    def test2(self):
        nums,k,t = [1,0,1,1],  1, 2
        Output= True
        self.assertEqual(Output, get_sol().containsNearbyAlmostDuplicate(nums,k,t))
    def test3(self):
        nums,k,t = [1,5,9,1,5,9],  2, 3
        Output= False
        self.assertEqual(Output, get_sol().containsNearbyAlmostDuplicate(nums,k,t))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
