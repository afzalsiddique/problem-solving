import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in range(len(encoded)):
            res.append(res[i]^encoded[i])
        return res



