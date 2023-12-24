from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list,ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
# def get_sol(*args): return Solution().peakIndexInMountainArray(*args)
def get_sol(): return HitCounter()


class HitCounter:
    def __init__(self):
        self.q=deque()
    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)
    def getHits(self, timestamp: int) -> int:
        while self.q and self.q[0]<=timestamp-300:
            self.q.popleft()
        return len(self.q)

