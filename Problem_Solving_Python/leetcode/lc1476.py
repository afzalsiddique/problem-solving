import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(x): return SubrectangleQueries(x)
class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.rectangle=rectangle
        self.li = []
    def updateSubrectangle(self, r1: int, c1: int, r2: int, c2: int, newValue: int) -> None:
        self.li.append((r1,c1,r2,c2,newValue))
    def getValue(self, row: int, col: int) -> int:
        i=len(self.li)-1
        while i>=0:
            r1,c1,r2,c2,newValue = self.li[i]
            if r1<=row<=r2 and c1<=col<=c2:
                return newValue
            i-=1
        return self.rectangle[row][col]
