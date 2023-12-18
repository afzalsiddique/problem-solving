from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n=len(intervals)
        if n<2:return True
        intervals.sort()
        last_end=intervals[0][1]
        for i in range(1,n):
            start,end=intervals[i]
            if start<last_end:
                return False
            last_end=end
        return True


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(False, get_sol().canAttendMeetings([[0,30],[5,10],[15,20]]))
    def test2(self):
        self.assertEqual(True, get_sol().canAttendMeetings([[7,10],[2,4]]))
    def test3(self):
        self.assertEqual(True, get_sol().canAttendMeetings([]))
    def test4(self):
        self.assertEqual(True, get_sol().canAttendMeetings([[13,15],[1,13]]))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):
