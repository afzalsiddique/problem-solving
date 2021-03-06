import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n==1: return intervals

        intervals.sort(key=lambda x:x[0])
        last_start, last_end = intervals[0][0], intervals[0][1]
        result = []
        for i in range(1,n):
            cur_start, cur_end = intervals[i][0],intervals[i][1]
            if cur_start>last_end:
                result.append([last_start,last_end])
                last_start = cur_start
            last_end = max(last_end, cur_end)
        result.append([last_start, last_end])
        return result
class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        res = []
        intervals.sort()
        res.append([intervals[0][0],intervals[0][1]])
        for i in range(1,n):
            new_start,new_end=intervals[i][0],intervals[i][1]
            last_start,last_end=res[-1][0],res[-1][1]
            if last_start<=new_start<=last_end or last_start<=new_end<=last_end:
                res[-1][0]=min(new_start,last_start)
                res[-1][1]=max(new_end,last_end)
            else:
                res.append([new_start,new_end])
        return res
class Solution3:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n,results= len(intervals),[]
        intervals.sort(key=lambda x:x[0])
        start,end = intervals[0][0],intervals[0][1]
        for i in range(n):
            cur_start,cur_end = intervals[i][0],intervals[i][1]
            if cur_start<=end: # overlapping. So move end
                end = max(cur_end, end)
            else: # non-overlapping. add previous
                results.append([start,end])
                start=cur_start
                end = cur_end
        results.append([start,end])
        return results

class Solution4:
    # the idea is that for the result distinct interval, the latter one's start must > previous one's end.
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        starts = sorted([x[0] for x in intervals])
        ends = sorted([x[1] for x in intervals])
        results = []
        i,j=0,0 #  starts[j] is start of new interval
        while i<n:
            if i==n-1 or ends[i]<starts[i+1]:
                results.append([starts[j],ends[i]])
                j=i+1
            i+=1
        return results
class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual([[1,6],[8,10],[15,18]],get_sol().merge([[1,3],[2,6],[8,10],[15,18]]))
    def test_2(self):
        self.assertEqual([[1,7],[8,10],[15,18]],get_sol().merge([[1,3],[2,6],[5,7],[8,10],[15,18]]))
    def test_3(self):
        self.assertEqual([[1,5]],get_sol().merge([[1,4],[4,5]]))
    def test_4(self):
        self.assertEqual([[0,4]],get_sol().merge([[1,4],[0,4]]))
    def test_5(self):
        self.assertEqual([[1,4]],get_sol().merge([[1,4],[2,3]]))
    def test_6(self):
        self.assertEqual([[1,10]],get_sol().merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
