from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import cache; from heapq import *; import unittest; from typing import List, Optional; import functools;from sortedcontainers import SortedList,SortedDict
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return MyCalendarTwo()
class MyCalendarTwo:
    def __init__(self):
        self.booking = []
        self.double_booking = []

    def book(self, start, end):
        for i, j in self.double_booking:
            if start < j and end > i:
                return False
        for i, j in self.booking:
            if start < j and end > i:
                self.double_booking.append((max(start, i), min(end, j)))
                # break # wrong
        self.booking.append((start, end))
        return True
class MyCalendarTwo2:
    # TreeMap or SortedDict()
    # vertical laser scanning similar to line sweep
    def __init__(self):
        self.di=SortedDict()
    def book(self, start: int, end: int) -> bool:
        di=self.di
        if start not in di:
            di[start]=0
        di[start]+=1

        if end not in di:
            di[end]=0
        di[end]-=1

        cnt=0
        for point in di:
            cnt+=di[point]
            if cnt>2:
                di[start]-=1
                if di[start]==0:
                    di.pop(start)
                di[end]+=1
                if di[end]==0:
                    di.pop(end)
                return False
        return True
class Tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='MyCalendarTwo': obj = get_sol(); outputs.append(None)
            elif cmd=='book': outputs.append(obj.book(input[0],input[1]))
        return outputs
    def test_01(self):
        commands = ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
        inputs=[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
        expected = [None, True, True, True, False, True, True]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_02(self):
        commands = ["MyCalendarTwo","book","book","book","book","book","book","book","book","book","book"]
        inputs=[[],[24,40],[43,50],[27,43],[5,21],[30,40],[14,29],[3,19],[3,14],[25,39],[6,19]]
        expected = [None,True,True,True,True,False,False,True,False,False,False]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_03(self):
        commands = ["MyCalendarTwo","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book"]
        inputs=[[],[5,12],[42,50],[4,9],[33,41],[2,7],[16,25],[7,16],[6,11],[13,18],[38,43],[49,50],[6,15],[5,13],[35,42],[19,24],[46,50],[39,44],[28,36],[28,37],[20,29],[41,49],[11,19],[41,46],[28,37],[17,23],[22,31],[4,10],[31,40],[4,12],[19,26]]
        expected = [None,True,True,True,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_04(self):
        commands = ["MyCalendarTwo","book","book","book","book"]
        inputs=[[],[42,50],[33,41],[38,43],[35,42]]
        expected = [None, True, True, True, False]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
