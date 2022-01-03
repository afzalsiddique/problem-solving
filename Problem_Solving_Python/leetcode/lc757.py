import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        intervals.sort(key=lambda x:(x[1],-x[0]))
        res=2
        last=intervals[0][1]
        second_last=last-1
        for i in range(1,n):
            a,b=intervals[i]
            if a>last:
                res+=2
                last=b
                second_last=b-1
            elif a>second_last:
                res+=1
                second_last=last
                last=b
        return res



class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(3,get_sol().intersectionSizeTwo([[1,3],[1,4],[2,5],[3,5]]))
    def test02(self):
        self.assertEqual(5,get_sol().intersectionSizeTwo([[1,2],[2,3],[2,4],[4,5]]))
    def test03(self):
        self.assertEqual(4,get_sol().intersectionSizeTwo([[18,24],[24,33],[29,37]]))
    # def test04(self):
    # def test05(self):
    # def test06(self):
