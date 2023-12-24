from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list,ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(*args): return Solution().maxValue(*args)


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def get_min_sum(available_space, max_value):
            a = max_value
            if a > available_space:
                b = a - available_space
                return a * (a + 1) // 2 - b * (b + 1) // 2
            return a * (a + 1) // 2 + (available_space - a)

        space_on_left, space_on_right = index, n - index - 1
        l, r = 0, maxSum
        while l <= r:
            mid = (l + r) // 2
            left = get_min_sum(space_on_left, mid - 1)
            right = get_min_sum(space_on_right, mid - 1)
            if left + mid + right <= maxSum:
                l = mid + 1
            else:
                r = mid - 1
        return max(1,l - 1)


Cases=[
    4, 2, 6,
    6, 1, 10,
    4,0,4
]
Expected=[2,3,1]
PARAMETERS=3

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
    def test03(self):
        testNo=3
        self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    def test04(self):
        testNo=4
        self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    def test05(self):
        testNo=5
        self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))


