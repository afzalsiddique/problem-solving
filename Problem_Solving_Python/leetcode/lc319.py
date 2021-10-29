import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/bulb-switcher/discuss/77104/Math-solution..
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))

