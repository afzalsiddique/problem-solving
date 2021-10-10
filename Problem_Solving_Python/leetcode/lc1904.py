import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        startHour,startMin, finishHour,finishMin = int(startTime[:2]),int(startTime[3:]) ,int(finishTime[:2]),int(finishTime[3:])
        if startTime>finishTime:
            finishHour+= 24
        start = (startHour*60+startMin) # convert it to minutes
        finish = (finishHour*60+finishMin) # convert it to minutes
        start = math.ceil(start/15) # move this to the closest next slot
        finish = math.floor(finish/15) # move this to the closest previous slot
        return max(0,finish - start)


class MyTestCase(unittest.TestCase):
    def test1(self):
        startTime,finishTime = "12:01",  "12:44"
        Output= 1
        self.assertEqual(Output, get_sol().numberOfRounds(startTime, finishTime))
    def test2(self):
        startTime,finishTime = "20:00",  "06:00"
        Output= 40
        self.assertEqual(Output, get_sol().numberOfRounds(startTime, finishTime))
    def test3(self):
        startTime,finishTime = "00:00",  "23:59"
        Output= 95
        self.assertEqual(Output, get_sol().numberOfRounds(startTime, finishTime))
    def test4(self):
        startTime,finishTime = "06:01",  "06:50"
        Output= 2
        self.assertEqual(Output, get_sol().numberOfRounds(startTime, finishTime))
    def test5(self):
        startTime,finishTime = "06:00",  "06:20"
        Output= 1
        self.assertEqual(Output, get_sol().numberOfRounds(startTime, finishTime))
    def test6(self):
        startTime,finishTime = "06:00",  "06:30"
        Output= 2
        self.assertEqual(Output, get_sol().numberOfRounds(startTime, finishTime))
    def test7(self):
        startTime,finishTime = "06:00",  "08:00"
        Output= 8
        self.assertEqual(Output, get_sol().numberOfRounds(startTime, finishTime))
    def test8(self):
        startTime,finishTime = "00:01",  "00:00"
        Output= 95
        self.assertEqual(Output, get_sol().numberOfRounds(startTime, finishTime))
    def test9(self):
        startTime,finishTime = "23:46", "00:01"
        Output= 0
        self.assertEqual(Output, get_sol().numberOfRounds(startTime, finishTime))
    def test10(self):
        startTime,finishTime = "14:41", "15:24"
        Output= 2
        self.assertEqual(Output, get_sol().numberOfRounds(startTime, finishTime))
    def test11(self):
        startTime,finishTime = "00:47", "00:57"
        Output= 0
        self.assertEqual(Output, get_sol().numberOfRounds(startTime, finishTime))
