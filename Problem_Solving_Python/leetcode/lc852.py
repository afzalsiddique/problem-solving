from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list,ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(*args): return Solution().peakIndexInMountainArray(*args)
# def get_sol(): return Solution()

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        l,r=0,n-1
        while l<=r:
            m=(l+r)//2
            # if arr[m] >= arr[m + 1]: # also works
            if arr[m]>arr[m+1]:
                r = m - 1
            else:
                l = m + 1
        return l
class Solution2:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        l,r=0,n-1
        while l<r:
            m=(l+r)//2
            # if arr[m] >= arr[m + 1]: # also works
            if arr[m]>arr[m+1]:
                r = m
            else:
                l=m+1
        return l

Cases=[
    [0, 1, 0],
    [0, 2, 1, 0],
    [0, 10, 5, 2],
    [3, 4, 5, 1]
]
PARAMETERS=1
Expected=[1,1,1,2]


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


