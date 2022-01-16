import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n=len(nums)
        i=j=k
        res=nums[k]
        curMin=nums[k]
        while i-1>=0 and j+1<n:
            if nums[i-1]<nums[j+1]:
                j+=1
            else:
                i-=1
            curMin=min(curMin,nums[i],nums[j])
            res=max(res,curMin*(j-i+1))
        while i-1>=0:
            i-=1
            curMin=min(curMin,nums[i],nums[j])
            res=max(res,curMin*(j-i+1))
        while j+1<n:
            j+=1
            curMin=min(curMin,nums[i],nums[j])
            res=max(res,curMin*(j-i+1))
        return res

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(15,get_sol().maximumScore([1,4,3,7,4,5],3))
    def test2(self):
        self.assertEqual(20,get_sol().maximumScore([5,5,4,5,4,1,1,1], 0))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
