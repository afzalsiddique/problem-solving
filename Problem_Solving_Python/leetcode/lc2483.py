from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list,ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(*args): return Solution().bestClosingTime(*args)
# def get_sol(): return Solution()

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        left = [0] + list(accumulate([1 if c == 'N' else 0 for c in customers]))
        right = ([0] + list(accumulate([1 if c == 'Y' else 0 for c in customers[::-1]])))[::-1]
        ret_idx = -1
        ret_val = float('inf')
        for i in range(n + 1):
            if left[i] + right[i] < ret_val:
                ret_val = left[i] + right[i]
                ret_idx = i
        return ret_idx


Cases=[
    "YYNY",
    "NNNNN",
    "YYYY"
]
PARAMETERS=1
Expected=[2,0,4]


class MyTestCase(unittest.TestCase):
    def test00(self):
        testNo=0
        self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    def test01(self):
        testNo=1
        self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    def test02(self):
        testNo=2
        self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    # def test03(self):
    #     testNo=3
    #     self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    # def test04(self):
    #     testNo=4
    #     self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    # def test05(self):
    #     testNo=5
    #     self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))


