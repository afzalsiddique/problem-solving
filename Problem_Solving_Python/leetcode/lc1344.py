import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutes_percentage = minutes/60
        minutes = minutes*6
        hour = (hour%12)*30 + minutes_percentage*30
        return min(abs(minutes-hour),abs(hour- minutes))

class MyTestCase(unittest.TestCase):
    def test1(self):
        hour,minutes = 12,  30
        Output= 165
        self.assertEqual(Output, get_sol().angleClock(hour,minutes))
    def test2(self):
        hour,minutes = 3,  30
        Output= 75
        self.assertEqual(Output, get_sol().angleClock(hour,minutes))
    def test3(self):
        hour,minutes = 3,  15
        Output= 7.5
        self.assertEqual(Output, get_sol().angleClock(hour,minutes))
    def test4(self):
        hour,minutes = 4,  50
        Output= 155
        self.assertEqual(Output, get_sol().angleClock(hour,minutes))
    def test5(self):
        hour,minutes = 12,  0
        Output= 0
        self.assertEqual(Output, get_sol().angleClock(hour,minutes))
    def test6(self):
        hour,minutes = 1, 57
        Output= 283.5
        self.assertEqual(Output, get_sol().angleClock(hour,minutes))
    # def test7(self):
