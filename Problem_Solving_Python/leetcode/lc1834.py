import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n=len(tasks)
        tmp=[(tasks[i][0],tasks[i][1],i) for i in range(n)] # arrival,processing_time,idx
        tasks=sorted(tmp) # sort based on arrival time
        i=0
        res=[]
        pq=[]
        cur_time=tasks[0][0]
        while len(res)<n:
            while i<n and tasks[i][0]<=cur_time:
                _,processing_time,idx=tasks[i]
                heappush(pq,[processing_time,idx])
                i+=1
            if pq: # if we have some tasks to do
                processing_time,idx=heappop(pq)
                cur_time+=processing_time
                res.append(idx)
            else: # if we do not have any task
                if i<n:
                    cur_time = tasks[i][0] # go to the next task if exists

        return res
class MyTestCase(unittest.TestCase):
    def test_1(self):
        tasks = [[1,2],[2,4],[3,2],[4,1]]
        Output= [0,2,3,1]
        self.assertEqual(Output, get_sol().getOrder(tasks))
    def test_2(self):
        tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
        Output= [4,3,2,0,1]
        self.assertEqual(Output, get_sol().getOrder(tasks))
    def test_3(self):
        tasks = [[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]
        Output= [6,1,2,9,4,10,0,11,5,13,3,8,12,7]
        self.assertEqual(Output, get_sol().getOrder(tasks))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
