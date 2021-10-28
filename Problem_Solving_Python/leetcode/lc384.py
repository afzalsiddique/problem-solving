import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(x): return Solution(x)
class Solution:
    # Fisher-Yates
    # https://www.youtube.com/watch?v=tLxBwSL3lPQ
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.copy = nums[:]
    def reset(self) -> List[int]:
        self.nums = self.copy[:]
        return self.nums
    def shuffle(self) -> List[int]:
        nums = self.nums
        n=len(nums)
        for i in range(n-1,-1,-1):
            j = random.randint(0,i)
            nums[i],nums[j]=nums[j],nums[i]
        return nums