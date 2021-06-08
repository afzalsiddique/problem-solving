import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
# def get_sol(): return Solution()
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
        self.booking.append((start, end))
        return True