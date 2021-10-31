import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n=len(events)
        li = [float('-inf')]*(n+1)
        events.sort(key=lambda x:x[1])
        endtimes = [x[1] for x in events] # sorted endtimes
        events.sort(key=lambda x:(x[0], x[2]))
        i,j=n-1,n-1
        while i>=0 and j>=0:
            start,_,val = events[i]
            end = endtimes[j]
            if start>end:
                li[j]=max(li[j],li[j+1], val)
                i-=1
            else:
                li[j]=max(li[j],li[j+1])
                j-=1
        while j>=0:
            li[j]=li[j+1]
        di = defaultdict(int)
        for i in range(len(endtimes)):
            di[endtimes[i]]=max(di[endtimes[i]],li[i])

        maxx = 0
        for i in range(len(events)):
            _,end, val = events[i]
            maxx = max(maxx, val+di[end])
        max_value = max(x[2] for x in events)
        maxx = max(maxx, max_value)
        return maxx


class MyTestCase(unittest.TestCase):
    def test1(self):
        events = [[1,3,2],[4,5,2],[2,4,3]]
        Output= 4
        self.assertEqual(Output, get_sol().maxTwoEvents(events))
    def test2(self):
        events = [[1,3,2],[4,5,2],[1,5,5]]
        Output= 5
        self.assertEqual(Output, get_sol().maxTwoEvents(events))
    def test3(self):
        events = [[1,5,3],[1,5,1],[6,6,5]]
        Output= 8
        self.assertEqual(Output, get_sol().maxTwoEvents(events))
    def test4(self):
        events = [[10,83,53],[63,87,45],[97,100,32],[51,61,16]]
        Output= 85
        self.assertEqual(Output, get_sol().maxTwoEvents(events))
    # def test5(self):
    # def test6(self):

