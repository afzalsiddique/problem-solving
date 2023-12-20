from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list,ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(*args): return Solution().maxValue(*args)

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def sum_range(lo, hi): # both inclusive
            if lo>hi: return 0
            if lo<=0: lo=1
            return hi * (hi + 1) // 2 - (lo - 1) * lo // 2
        def valid(mid):
            hi=mid-1
            lo = mid-items_on_the_left
            sum_left = sum_range(lo,hi)

            hi=mid-1
            lo=mid-items_on_the_right
            sum_right=sum_range(lo,hi)

            minn= sum_left+mid+sum_right
            return minn<=maxSum

        maxSum-=n # subtract 1 from every item in the array. the condition becomes A[i]>=0
        if maxSum==0: return 1
        items_on_the_right=n-index-1
        items_on_the_left = index
        left=0
        right=maxSum+1
        while left<=right:
            mid = (left+right)//2
            if valid(mid-1): # subtract 1 from every item in the array. the condition becomes A[i]>=0
                left=mid+1
            else:
                right=mid-1
        return left-1

class Solution2:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def sum_up_to_n(n): return n*(n+1)//2
        def get_min_sum(available_space, max_value):
            a = max_value
            if a > available_space:
                b = a - available_space
                return sum_up_to_n(a) - sum_up_to_n(b)
            return sum_up_to_n(a) + (available_space - a)

        space_on_left, space_on_right = index, n - index - 1
        l, r = 0, maxSum
        while l <= r:
            mid = (l + r) // 2
            left_sum = get_min_sum(space_on_left, mid - 1)
            right_sum = get_min_sum(space_on_right, mid - 1)
            if left_sum + mid + right_sum <= maxSum:
                l = mid + 1
            else:
                r = mid - 1
        return max(1,l - 1)


Cases=[
    4, 2, 6,
    6, 1, 10,
    4,0,4,
    8,7,14
]
Expected=[2,3,1,4]
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


