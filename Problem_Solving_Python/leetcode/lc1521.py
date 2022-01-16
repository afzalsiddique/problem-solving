import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # time and space O(n*log(max(arr[i]))
    def closestToTarget(self, arr: List[int], target: int) -> int:
        n=len(arr)
        sets=[set() for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            sets[i].add(arr[i])
            for x in sets[i+1]:
                sets[i].add(x&arr[i])

        res=float('inf')
        for i in range(n):
            for x in sets[i]:
                res=min(res,abs(x-target))
        return res
class Solution2:
    # time O(n*log(max(arr[i]))
    # space O(log(max(arr[i]))
    def closestToTarget(self, arr: List[int], target: int) -> int:
        n=len(arr)
        res=float('inf')
        prevSet=set()
        for i in range(n-1,-1,-1):
            curSet=set()
            curSet.add(arr[i])
            for x in prevSet:
                curSet.add(x&arr[i])
            for x in curSet:
                res=min(res,abs(x-target))
            prevSet=curSet
        return res

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(2,get_sol().closestToTarget([9,12,3,7,15],  5))
    def test2(self):
        self.assertEqual(999999,get_sol().closestToTarget([1000000,1000000,1000000],  1))
    def test3(self):
        self.assertEqual(0,get_sol().closestToTarget([1,2,4,8,16], 0))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
