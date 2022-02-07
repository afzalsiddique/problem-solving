from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0: return [newInterval]
        start=[x[0] for x in intervals]
        end=[x[1] for x in intervals]
        idx=bisect_left(start,newInterval[0])
        start=start[:idx]+[newInterval[0]]+start[idx:]
        end=end[:idx]+[newInterval[1]]+end[idx:]
        intervals = [[s,e] for s,e in zip(start,end)]
        return self.merge(intervals)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]: # same as leetcode 56 merge interval
        intervals.sort()
        res=[]
        lastStart=intervals[0][0]
        lastEnd=intervals[0][1]
        for s,e in intervals[1:]:
            if s<=lastEnd:
                lastEnd=max(lastEnd,e)
            else:
                res+=[[lastStart,lastEnd]]
                lastStart,lastEnd=s,e
        res+=[[lastStart,lastEnd]]
        return res
class Solution2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals+=[newInterval]
        return self.merge(intervals)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]: # same as leetcode 56 merge interval
        intervals.sort()
        res=[]
        lastStart=intervals[0][0]
        lastEnd=intervals[0][1]
        for s,e in intervals[1:]:
            if s<=lastEnd:
                lastEnd=max(lastEnd,e)
            else:
                res+=[[lastStart,lastEnd]]
                lastStart,lastEnd=s,e
        res+=[[lastStart,lastEnd]]
        return res

class MyTestCase(unittest.TestCase):
    def test001(self):
        self.assertEqual([[1,5],[6,9]], get_sol().insert([[1,3],[6,9]], [2,5]))
    def test002(self):
        self.assertEqual([[1,2],[3,10],[12,16]], get_sol().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
    def test003(self):
        self.assertEqual([[5,7]],get_sol().insert([], [5,7]))
    def test01(self):
        self.assertEqual([[1,6],[8,10],[15,18]],get_sol().merge([[1,3],[2,6],[8,10],[15,18]]))
    def test02(self):
        self.assertEqual([[1,7],[8,10],[15,18]],get_sol().merge([[1,3],[2,6],[5,7],[8,10],[15,18]]))
    def test03(self):
        self.assertEqual([[1,5]],get_sol().merge([[1,4],[4,5]]))
    def test04(self):
        self.assertEqual([[0,4]],get_sol().merge([[1,4],[0,4]]))
    def test05(self):
        self.assertEqual([[1,4]],get_sol().merge([[1,4],[2,3]]))
    def test06(self):
        self.assertEqual([[1,10]],get_sol().merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
