from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; import functools
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    def countElements(self, nums: List[int]) -> int:
        count=Counter(nums)
        minn=min(nums)
        maxx=max(nums)
        total=sum(count.values())
        total-=count[minn]
        total-=count[maxx]
        return max(0,total)
