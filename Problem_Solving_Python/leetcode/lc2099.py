import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        pq=[]
        i=0
        while i<k:
            heappush(pq,(nums[i],i))
            i+=1
        while i<n:
            if pq[0][0]<nums[i]:
                heappop(pq)
                heappush(pq,(nums[i],i))
            i+=1

        pq.sort(key=lambda x:x[1])
        res=[x[0] for x in pq]
        return res


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual([3,3], get_sol().maxSubsequence(nums = [2,1,3,3], k = 2))
    def test2(self):
        self.assertEqual([-1,3,4], get_sol().maxSubsequence(nums = [-1,-2,3,4], k = 3))
    def test3(self):
        self.assertEqual([3,4], get_sol().maxSubsequence(nums = [3,4,3,3], k = 2))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):