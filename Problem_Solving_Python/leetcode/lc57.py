import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0: return [newInterval]
        res=[]
        start=[x[0] for x in intervals]
        end=[x[1] for x in intervals]
        idx=bisect_left(start,newInterval[0])
        start=start[:idx]+[newInterval[0]]+start[idx:]
        end=end[:idx]+[newInterval[1]]+end[idx:]

        last_start,last_end=start[0],end[0]
        for i in range(1,len(start)):
            cur_start,cur_end=start[i],end[i]
            if cur_start>last_end:
                res.append([last_start,last_end])
                last_start=cur_start
            last_end=max(last_end,cur_end)
        res.append([last_start,last_end])
        return res


class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([[1,5],[6,9]],Solution().insert([[1,3],[6,9]] ,[2,5]))
    def test2(self):
        self.assertEqual([[1,7]],Solution().insert([[1,5]], [1,7]))
    def test3(self):
        self.assertEqual([[5,7]],Solution().insert([], [5,7]))
