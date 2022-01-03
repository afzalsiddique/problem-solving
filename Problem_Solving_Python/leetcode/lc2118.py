import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num==0: return True
        s=str(num)
        if s[0]=='0' or s[-1]=='0':
            return False
        return True

