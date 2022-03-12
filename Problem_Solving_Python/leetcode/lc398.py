import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(x): return Solution(x)
class Solution:
    # reservoir sampling
    def __init__(self, nums: List[int]):
        self.nums = nums
    def pick(self, target: int) -> int:
        count = 0
        res = -1
        for i in range(len(self.nums)):
            if self.nums[i]!=target: continue
            if random.randint(0,count)==0:
                res=i
            count+=1
        return res
class Solution2:
    # problem: uses more memory
    def __init__(self, nums: List[int]):
        self.di = defaultdict(list)
        for i,x in enumerate(nums):
            self.di[x].append(i)
    def pick(self, target: int) -> int:
        idx = random.randint(0,len(self.di[target]))
        return self.di[target][idx]
