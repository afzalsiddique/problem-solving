import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count=Counter(nums)
        if count[1]==0:
            return 0
        if count[0]==0:
            return 0
        targetOnes=count[1]
        nums=nums[:]+nums[:]
        n=len(nums)
        i=0
        j=0
        ones=0
        zeros=0
        res=float('inf')
        while i<targetOnes-1:
            if nums[i]==1:
                ones+=1
            else:
                zeros+=1
            i+=1
        while i<n:
            if nums[i]==1:
                ones+=1
            else:
                zeros+=1
            i+=1

            res=min(res,zeros)

            if nums[j]==1:
                ones-=1
            else:
                zeros-=1
            j+=1

        return res


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, get_sol().minSwaps([0,1,0,1,1,0,0]))
    def test2(self):
        self.assertEqual(2, get_sol().minSwaps([0,1,1,1,0,0,1,1,0]))
    def test3(self):
        self.assertEqual(0, get_sol().minSwaps([1,1,0,0,1]))
    def test4(self):
        self.assertEqual(0, get_sol().minSwaps([0,0,0]))
    def test5(self):
        self.assertEqual(1, get_sol().minSwaps([1,1,1,0,0,1,0,1,1,0]))
    # def test6(self):
    # def test7(self):
