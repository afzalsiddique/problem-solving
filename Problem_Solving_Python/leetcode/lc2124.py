import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def checkString(self, s: str) -> bool:
        bFound=False
        for x in s:
            if x=='b':
                bFound=True
            if bFound and x=='a':
                return False
        return True



