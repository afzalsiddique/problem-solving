import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools;from sortedcontainers import SortedList
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        def withinRange(x,start,end): return start<=x<=end
        n=len(queries)
        queries=[[q,i] for i,q in enumerate(queries)]
        queries.sort()
        intervals.sort()
        res=[-1 for _ in range(n)]
        pq=[]
        i=0
        for q,idx in queries:
            while i<len(intervals) and intervals[i][0]<=q:
                start,end=intervals[i]
                size=end-start+1
                heappush(pq,(size,start,end))
                i+=1
            while pq and not withinRange(q,pq[0][1],pq[0][2]):
                heappop(pq)
            if pq:
                res[idx]=pq[0][0]
        return res

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([3,3,1,4],get_sol().minInterval( [[1,4],[2,4],[3,6],[4,4]], [2,3,4,5]))
    def test2(self):
        self.assertEqual([2,-1,4,6],get_sol().minInterval( [[2,3],[2,5],[1,8],[20,25]], [2,19,5,22]))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
