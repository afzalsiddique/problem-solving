from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=3oDvuHCTFmY
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        if n==1: return 0
        intervals.sort(key=lambda x:x[1])
        last_start,last_end=intervals[0][0],intervals[0][1]
        res=[]
        for i in range(1,n):
            cur_start,cur_end=intervals[i][0],intervals[i][1]
            if cur_start>=last_end:
                res.append([last_start,last_end])
                last_start=cur_start
                last_end=cur_end
        res.append([last_start,last_end])
        # print(res)
        return n-len(res)

class tester(unittest.TestCase):
    def test1(self):
        intervals = [[1,2],[2,3],[3,4],[1,3]]
        Output= 1
        self.assertEqual(Output,get_sol().eraseOverlapIntervals(intervals))
    def test2(self):
        intervals = [[1,2],[1,2],[1,2]]
        Output= 2
        self.assertEqual(Output,get_sol().eraseOverlapIntervals(intervals))
    def test3(self):
        intervals = [[1,2],[2,3]]
        Output= 0
        self.assertEqual(Output,get_sol().eraseOverlapIntervals(intervals))
    def test4(self):
        intervals = [[2,3],[4,5],[1,6]]
        Output= 1
        self.assertEqual(Output,get_sol().eraseOverlapIntervals(intervals))
    def test5(self):
        intervals = [[1,4],[3,6],[1,8]]
        Output= 2
        self.assertEqual(Output,get_sol().eraseOverlapIntervals(intervals))
    def test6(self):
        intervals = [[0,10],[5,12]]
        Output= 1
        self.assertEqual(Output,get_sol().eraseOverlapIntervals(intervals))
    def test7(self):
        intervals = [[1,2]]
        Output= 0
        self.assertEqual(Output,get_sol().eraseOverlapIntervals(intervals))
    def test8(self):
        intervals = [[1,100],[11,22],[1,11],[2,12]]
        Output= 2
        self.assertEqual(Output,get_sol().eraseOverlapIntervals(intervals))
