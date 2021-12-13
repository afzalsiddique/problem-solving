import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def countPoints(self, rings: str) -> int:
        n=len(rings)
        i=0
        arr=[set() for _ in range(10)]
        while i<n:
            arr[int(rings[i+1])].add(rings[i])
            i+=2
        return sum([True for x in arr if len(x)==3])
