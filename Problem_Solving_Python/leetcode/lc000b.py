import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        _sum, _max = sum(milestones), max(milestones)
        if _sum - _max >= _max:
            return _sum
        return 2 * (_sum - _max) + 1  # start from the project with most milestones (_sum - _max + 1) and work on the the rest of milestones (_sum - _max)


class tester(unittest.TestCase):
    def test_1(self):
        num = "132"
        change = [9,8,5,0,3,6,4,2,6,8]
        Output= "832"
        self.assertEqual(Output, get_sol().maximumNumber(num,change))
    def test_2(self):
        num = "021"
        change = [9,4,3,5,7,2,1,9,0,6]
        Output= "934"
        self.assertEqual(Output, get_sol().maximumNumber(num,change))
    def test_3(self):
        num = "5"
        change = [1,4,7,5,3,2,5,6,9,4]
        Output= "5"
        self.assertEqual(Output, get_sol().maximumNumber(num,change))
    def test_4(self):
        num = "214010"
        change = [6,7,9,7,4,0,3,4,4,7]
        Output= "974676"
        self.assertEqual(Output, get_sol().maximumNumber(num,change))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
