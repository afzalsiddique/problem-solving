from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list,ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(*args): return Solution().validPartition(*args)
# def get_sol(): return Solution()

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @cache
        def dp(i):
            if i == n: return True
            equal2, equal3, consec3 = False, False, False
            if i + 1 < n and nums[i] == nums[i + 1]:
                equal2 = dp(i + 2)
            if i + 2 < n and nums[i] == nums[i + 1] == nums[i + 2]:
                equal3 = dp(i + 3)
            if i + 2 < n and nums[i] + 1 == nums[i + 1] and nums[i + 1] + 1 == nums[i + 2]:
                consec3 = dp(i + 3)
            return equal2 or equal3 or consec3

        n = len(nums)
        return dp(0)

Cases=[
    [4, 4, 4, 5, 6],
    [1, 1, 1, 2]
]
PARAMETERS=1
Expected=[True,False]


class MyTestCase(unittest.TestCase):
    def test00(self):
        testNo=0
        self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    def test01(self):
        testNo=1
        self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    # def test02(self):
    #     testNo=2
    #     self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    # def test03(self):
    #     testNo=3
    #     self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    # def test04(self):
    #     testNo=4
    #     self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    # def test05(self):
    #     testNo=5
    #     self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))


