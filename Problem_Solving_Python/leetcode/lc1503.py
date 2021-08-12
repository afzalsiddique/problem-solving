import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        r=[n-x for x in right] if right else [0]
        l=[x-0 for x in left] if left else [0]
        return max(max(l),max(r))


class MyTestCase(unittest.TestCase):
    def test_1(self):
        n,left,right= 4, [4,3],[0,1]
        Output= 4
        self.assertEqual(Output, get_sol().getLastMoment(n,left,right))
    def test_2(self):
        n,left,right= 7, [],[0,1,2,3,4,5,6,7]
        Output= 7
        self.assertEqual(Output, get_sol().getLastMoment(n,left,right))
    def test_3(self):
        n,left,right= 7, [0,1,2,3,4,5,6,7],[]
        Output= 7
        self.assertEqual(Output, get_sol().getLastMoment(n,left,right))
    def test_4(self):
        n,left,right= 9, [5],[4]
        Output= 5
        self.assertEqual(Output, get_sol().getLastMoment(n,left,right))
    def test_5(self):
        n,left,right= 6, [6],[0]
        Output= 6
        self.assertEqual(Output, get_sol().getLastMoment(n,left,right))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):