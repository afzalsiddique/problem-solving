import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=len(colors)
        maxx=0
        for i in range(n):
            for j in range(i+1,n):
                if colors[i]!=colors[j]:
                    maxx=max(maxx,j-i)
        return maxx
