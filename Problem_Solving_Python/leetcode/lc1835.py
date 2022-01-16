import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
     # (a&b) ^ (a&c) = a&(b^c)
     # (arr1[i]&arr2[0])^(arr1[i]&arr2[1]).. = arr1[i]&(arr2[0]^arr2[1]^arr[2]...)
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        xor=0
        for x in arr2:
            xor^=x

        res=0
        for x in arr1:
            res^=x&xor
        return res


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(0,get_sol().getXORSum([1,2,3],[6,5]))
    def test2(self):
        self.assertEqual(4,get_sol().getXORSum([12], [4]))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
