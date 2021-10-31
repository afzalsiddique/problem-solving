import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            if i%10==nums[i]:
                return i
        return -1


