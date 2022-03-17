from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid - 1
            else:
                l = mid + 1


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(3, get_sol().mySqrt(9))
    def test02(self):
        self.assertEqual(3, get_sol().mySqrt(10))
    def test03(self):
        self.assertEqual(2, get_sol().mySqrt(4))
    def test04(self):
        self.assertEqual(2, get_sol().mySqrt(8))
    def test05(self):
        self.assertEqual(0, get_sol().mySqrt(0))
    def test06(self):
        self.assertEqual(1, get_sol().mySqrt(1))
