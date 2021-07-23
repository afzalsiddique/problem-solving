import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        rungs = [0] + rungs
        n=len(rungs)
        ans=0
        for i in range(n-1):
            diff = rungs[i+1]-rungs[i]
            cnt = math.ceil(diff/dist) - 1
            ans+=cnt
        return ans
