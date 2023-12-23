from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list,ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(*args): return Solution().maxNonDecreasingLength(*args)
# def get_sol(): return Solution()

class Solution:
    # https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/solutions/3739198/java-c-python-dp/
    # dpA means the maximum step ending with A[i].
    # dpB means the maximum step ending with B[i].
    # Then consider these 4 transitions:
    # tA1 for A[i - 1] -> A[i]
    # tA2 for B[i - 1] -> A[i]
    # tB1 for A[i - 1] -> B[i]
    # tB2 for B[i - 1] -> B[i]
    # We update
    # dp1 = max(t11, t21)
    # dp2 = max(t12, t22)
    # res = max(res, dp1, dp2)
    def maxNonDecreasingLength(self, A: List[int], B: List[int]) -> int:
        res,dpA,dpB=1,1,1
        for i in range(1,len(A)):
            dpA1=dpA+1 if A[i]>=A[i-1] else 1
            dpA2=dpB+1 if A[i]>=B[i-1] else 1
            dpB1=dpA+1 if B[i]>=A[i-1] else 1
            dpB2=dpB+1 if B[i]>=B[i-1] else 1
            dpA=max(dpA1,dpA2)
            dpB=max(dpB1,dpB2)
            res=max(res,dpA,dpB)
        return res


Cases=[
    [2, 3, 1],[1, 2, 1],
    [1, 3, 2, 1], [2, 2, 3, 4],
    [1, 1], [2, 2],
    [3, 19, 13, 19],     [20, 18, 7, 14]
]
PARAMETERS=2
Expected=[2,4,2,2]


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
    # def test04(self):
    #     testNo=4
    #     self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    # def test05(self):
    #     testNo=5
    #     self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))


