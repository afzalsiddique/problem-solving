import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res=0
        for s in sentences:
            res=max(res,len(s.split()))
        return res

