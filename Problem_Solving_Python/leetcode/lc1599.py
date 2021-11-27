import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        maxx,prof=0,0
        run,max_run=0,0
        cur_sum=0
        summ=sum(customers)
        passengers=0
        i=0
        while passengers!=summ:
            if i<len(customers):
                cur_sum+=customers[i]
                i+=1
            new_people = min(cur_sum-passengers,4)
            passengers+=new_people
            prof += boardingCost*new_people - runningCost
            run+=1
            if prof>maxx:
                maxx=prof
                max_run=run
        return max_run if maxx!=0 else -1
class Solution2:
    # wrong
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        maxx,prof=0,0
        res=0
        cur_sum=0
        passengers = 0
        summ = sum(customers)
        i=0
        cnt=1
        while passengers!=summ:
            if i<len(customers):
                cur_sum+=customers[i]
                i+=1
            new_people =min(cur_sum,cnt*4)- passengers # wrong. taking more people in the next run if not enough people were taken in the previous run.
            passengers+=new_people
            prof += new_people*boardingCost-runningCost
            if prof>maxx:
                maxx=prof
                res=cnt
            cnt+=1
        return res if maxx!=0 else -1

class MyTestCase(unittest.TestCase):
    def test1(self):
        customers,boardingCost,runningCost = [8,3],  5,  6
        Output= 3
        self.assertEqual(Output, get_sol().minOperationsMaxProfit(customers,boardingCost,runningCost))
    def test2(self):
        customers,boardingCost,runningCost = [10,9,6],  6,  4
        Output= 7
        self.assertEqual(Output, get_sol().minOperationsMaxProfit(customers,boardingCost,runningCost))
    def test3(self):
        customers,boardingCost,runningCost = [3,4,0,5,1],  1,  92
        Output= -1
        self.assertEqual(Output, get_sol().minOperationsMaxProfit(customers,boardingCost,runningCost))
    def test4(self):
        customers,boardingCost,runningCost = [10,10,6,4,7],  3,  8
        Output= 9
        self.assertEqual(Output, get_sol().minOperationsMaxProfit(customers,boardingCost,runningCost))
    def test5(self):
        customers,boardingCost,runningCost = [0,10,4], 5, 3
        Output= 5
        self.assertEqual(Output, get_sol().minOperationsMaxProfit(customers,boardingCost,runningCost))
    def test6(self):
        customers,boardingCost,runningCost = [10,4], 5, 3
        Output= 4
        self.assertEqual(Output, get_sol().minOperationsMaxProfit(customers,boardingCost,runningCost))
    def test7(self):
        customers,boardingCost,runningCost = [0,43,37,9,23,35,18,7,45,3,8,24,1,6,37,2,38,15,1,14,39,27,4,25,27,33,43,8,44,30,38,40,20,5,17,27,43,11,6,2,30,49,30,25,32,3,18,23,45,43,30,14,41,17,42,42,44,38,18,26,32,48,37,5,37,21,2,9,48,48,40,45,25,30,49,41,4,48,40,29,23,17,7,5,44,23,43,9,35,26,44,3,26,16,31,11,9,4,28,49,43,39,9,39,37,7,6,7,16,1,30,2,4,43,23,16,39,5,30,23,39,29,31,26,35,15,5,11,45,44,45,43,4,24,40,7,36,10,10,18,6,20,13,11,20,3,32,49,34,41,13,11,3,13,0,13,44,48,43,23,12,23,2], 43, 54
        Output= 993
        self.assertEqual(Output, get_sol().minOperationsMaxProfit(customers,boardingCost,runningCost))
    def test8(self):
        customers,boardingCost,runningCost = [43,37,9,23,35,18,7,45,3,8,24,1,6,37,2,38,15,1,14,39,27,4,25,27,33,43,8,44,30,38,40,20,5,17,27,43,11,6,2,30,49,30,25,32,3,18,23,45,43,30,14,41,17,42,42,44,38,18,26,32,48,37,5,37,21,2,9,48,48,40,45,25,30,49,41,4,48,40,29,23,17,7,5,44,23,43,9,35,26,44,3,26,16,31,11,9,4,28,49,43,39,9,39,37,7,6,7,16,1,30,2,4,43,23,16,39,5,30,23,39,29,31,26,35,15,5,11,45,44,45,43,4,24,40,7,36,10,10,18,6,20,13,11,20,3,32,49,34,41,13,11,3,13,0,13,44,48,43,23,12,23,2], 43, 54
        Output= 992
        self.assertEqual(Output, get_sol().minOperationsMaxProfit(customers,boardingCost,runningCost))