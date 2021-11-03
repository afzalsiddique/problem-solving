import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(w,x,y): return Solution(w,x,y)
class Solution:
    # https://leetcode.com/problems/generate-random-point-in-a-circle/discuss/1113679/Python-Polar-coordinates-explained-with-diagrams-and-math
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x=x_center
        self.y=y_center
    def randPoint(self) -> List[float]:
        theta = random.uniform(0,2*math.pi) # radian
        r = self.r * math.sqrt(random.random())
        x = self.x + r * math.sin(theta) # takes radian input
        y = self.y + r * math.cos(theta)
        return [x,y]


class Solution2:
    # wrong
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x=x_center
        self.y=y_center
    def randPoint(self) -> List[float]:
        theta = random.randint(0,359)
        r = random.random() # [0,1). 1 not including
        r *= self.r
        x = self.x + r * math.sin(theta)
        y = self.y + r * math.cos(theta)
        return [x,y]
