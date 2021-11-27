import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        max1,min1=float('-inf'),float('inf')
        max2,min2=float('-inf'),float('inf')
        max3,min3=float('-inf'),float('inf')
        max4,min4=float('-inf'),float('inf')
        n=len(arr1)
        for i in range(n):
            max1 = max(max1,arr1[i] + arr2[i]+i)
            min1 = min(min1,arr1[i] + arr2[i]+i)

            max2 = max(max2,arr1[i] + arr2[i]-i)
            min2 = min(min2,arr1[i] + arr2[i]-i)

            max3 = max(max3,arr1[i] - arr2[i]+i)
            min3 = min(min3,arr1[i] - arr2[i]+i)

            max4 = max(max4,arr1[i] - arr2[i]-i)
            min4 = min(min4,arr1[i] - arr2[i]-i)
        return max(max1-min1, max2-min2, max3-min3, max4-min4)


class MyTestCase(unittest.TestCase):
    def test1(self):
        arr1,arr2 = [1,2,3,4],  [-1,4,5,6]
        Output= 13
        self.assertEqual(Output, get_sol().maxAbsValExpr(arr1,arr2))
    def test2(self):
        arr1,arr2 = [1,-2,-5,0,10],  [0,-2,-1,-7,-4]
        Output= 20
        self.assertEqual(Output, get_sol().maxAbsValExpr(arr1,arr2))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
