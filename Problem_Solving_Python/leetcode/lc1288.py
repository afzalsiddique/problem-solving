import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        cnt=1
        intervals.sort(key=lambda x:(-x[1],x[0]))
        last_begin,last_end = intervals[0][0],intervals[0][1]
        for i in range(1,n):
            cur_begin,cur_end = intervals[i][0],intervals[i][1]
            if cur_begin<last_begin:
                cnt+=1
                last_begin=cur_begin
        return cnt
class tester(unittest.TestCase):
    def test1(self):
        intervals = [[1,4],[3,6],[2,8]]
        Output= 2
        self.assertEqual(Output,Solution().removeCoveredIntervals(intervals))
    def test2(self):
        intervals = [[1,4],[2,3]]
        Output= 1
        self.assertEqual(Output,Solution().removeCoveredIntervals(intervals))
    def test3(self):
        intervals = [[0,10],[5,12]]
        Output= 2
        self.assertEqual(Output,Solution().removeCoveredIntervals(intervals))
    def test4(self):
        intervals = [[3,10],[4,10],[5,11]]
        Output= 2
        self.assertEqual(Output,Solution().removeCoveredIntervals(intervals))
    def test5(self):
        intervals = [[1,2],[1,4],[3,4]]
        Output= 1
        self.assertEqual(Output,Solution().removeCoveredIntervals(intervals))
