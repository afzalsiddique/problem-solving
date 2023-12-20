from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list,ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()

class Solution:
    # Instead of giving a single to a person
    # Give a set of cookies (using mask) to a single person
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def all_selected(mask): return mask == (1 << n) - 1
        @cache
        def solve(i, mask):
            if i == k:
                return 0 if all_selected(mask) else float('inf')
            res = float('inf')
            for new_mask in range(1 << n):
                if mask & new_mask != 0: continue
                tmpAns = solve(i + 1, mask | new_mask)
                res = min(res, max(dp_sum[new_mask], tmpAns))
            return res

        n = len(cookies)
        dp_sum = {} # pre calculate sum of different masks
        for mask in range(1 << n):
            tmpSum = 0
            for i in range(n):
                if (1 << i) & mask:
                    tmpSum += cookies[i]
            dp_sum[mask] = tmpSum

        return solve(0, 0)

Cases=[
    [8,15,10,20,8], 2,
    [8,15,10],2,
    [6,1,3,2,2,4,1,2], 3,
    [64,32,16,8,4,2,1,1000], 8,
    [10,15],2,
    [5,6,8,13,16,14,3,13],6
]
Expected=[31,18,7,1000,15,16]
PARAMETERS=2

class MyTestCase(unittest.TestCase):
    def test00(self):
        testNo=0
        self.assertEqual(Expected[testNo], get_sol().distributeCookies(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    def test01(self):
        testNo=1
        self.assertEqual(Expected[testNo], get_sol().distributeCookies(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    def test02(self):
        testNo=2
        self.assertEqual(Expected[testNo], get_sol().distributeCookies(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    def test03(self):
        testNo=3
        self.assertEqual(Expected[testNo], get_sol().distributeCookies(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    def test04(self):
        testNo=4
        self.assertEqual(Expected[testNo], get_sol().distributeCookies(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    def test05(self):
        testNo=5
        self.assertEqual(Expected[testNo], get_sol().distributeCookies(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))


