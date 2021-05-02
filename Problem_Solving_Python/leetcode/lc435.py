import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        if n==1: return 1
        intervals.sort(key=lambda x:(x[1],-x[0]))
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
        self.assertEqual(Output,Solution().eraseOverlapIntervals(intervals))
    def test2(self):
        intervals = [[1,2],[1,2],[1,2]]
        Output= 2
        self.assertEqual(Output,Solution().eraseOverlapIntervals(intervals))
    def test3(self):
        intervals = [[1,2],[2,3]]
        Output= 0
        self.assertEqual(Output,Solution().eraseOverlapIntervals(intervals))
    def test4(self):
        intervals = [[2,3],[4,5],[1,6]]
        Output= 1
        self.assertEqual(Output,Solution().eraseOverlapIntervals(intervals))
