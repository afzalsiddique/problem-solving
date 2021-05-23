import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n=len(intervals)
        res=[]
        di = {intervals[i][0]:i for i in range(n)}
        starts, ends = zip(*intervals)
        starts = sorted(starts)
        for i in range(n):
            end_time = intervals[i][1]
            idx = bisect_left(starts,end_time)
            if idx==n:
                res.append(-1)
            else:
                res.append(di[starts[idx]])
        return res

class MyTestCase(unittest.TestCase):

    def test_1(self):
        expected = [2,-1,-1,2,3]
        actual = get_sol().findRightInterval([[1,3],[1,4],[3,4],[2,3],[1,2]])
        self.assertEqual(expected, actual)

    def test_2(self):
        expected = [-1]
        actual = get_sol().findRightInterval([[1,2]])
        self.assertEqual(expected, actual)

    def test_3(self):
        expected = [-1,0,1]
        actual = get_sol().findRightInterval([[3,4],[2,3],[1,2]])
        self.assertEqual(expected, actual)

    def test_4(self):
        expected =[-1,2,-1]
        actual = get_sol().findRightInterval([[1,4],[2,3],[3,4]])
        self.assertEqual(expected, actual)

    def test_5(self):
        expected = [-1,0,1]
        actual = get_sol().findRightInterval([[4,5],[2,3],[1,2]])
        self.assertEqual(expected, actual)

