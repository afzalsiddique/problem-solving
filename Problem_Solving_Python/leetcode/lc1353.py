import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/discuss/510263/JavaC%2B%2BPython-Priority-Queue
    def maxEvents(self, events: List[List[int]]) -> int:
        n=len(events)
        BIG=10**5+1
        res=0
        events.sort(key=lambda x:x[0])
        pq=[] # all the events inside pq has already started
        i=0 # events iterator
        for cur_time in range(1,BIG):
            while i<n and events[i][0]==cur_time: # if the event already started, put it inside priority queue
                heappush(pq,events[i][1]) # heapify by end_time. We are trying to attend an event which already started and ends the soonest
                i+=1
            while pq and pq[0]<cur_time: # while end_time<cur_time i.e if the event already ended, take it out
                heappop(pq)
            if pq and cur_time<=pq[0]: # cur_time<=end_time
                heappop(pq)
                res+=1

        return res

class tester(unittest.TestCase):
    def test_1(self):
        events = [[1,2],[2,3],[3,4]]
        Output= 3
        self.assertEqual(Output, get_sol().maxEvents(events))
    def test_2(self):
        events= [[1,2],[2,3],[3,4],[1,2]]
        Output= 4
        self.assertEqual(Output, get_sol().maxEvents(events))
    def test_3(self):
        events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
        Output= 4
        self.assertEqual(Output, get_sol().maxEvents(events))
    def test_4(self):
        events = [[1,100000]]
        Output= 1
        self.assertEqual(Output, get_sol().maxEvents(events))
    def test_5(self):
        events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
        Output= 7
        self.assertEqual(Output, get_sol().maxEvents(events))
    def test_6(self):
        events = [[1,5],[1,5],[1,5],[2,3],[2,3]]
        Output= 5
        self.assertEqual(Output, get_sol().maxEvents(events))
    def test_7(self):
        events = [[1,2],[1,2],[1,6],[1,2],[1,2]]
        Output= 3
        self.assertEqual(Output, get_sol().maxEvents(events))
    # def test_8(self):