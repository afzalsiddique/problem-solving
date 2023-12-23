from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list,ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        # @cache
        def dp(i, last, li):
            # def dp(i,last):
            print(li)
            if i == n: return 0
            res = 0
            if nums1[i] >= last:
                # res=max(res,1+dp(i+1,nums1[i]))
                res = max(res, 1 + dp(i + 1, nums1[i], li + [nums1[i]]))
            if nums2[i] >= last:
                # res=max(res,1+dp(i+1,nums2[i]))
                res = max(res, 1 + dp(i + 1, nums2[i], li + [nums2[i]]))
            # res=max(res,dp(i+1,min(nums1[i],nums2[i])))
            res = max(res, dp(i + 1, min(nums1[i], nums2[i]), li + [min(nums1[i], nums2[i])]))
            return res

        n = len(nums1)
        # return dp(0,float('-inf'))
        return dp(0, float('-inf'), [])


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([0,3,1,2,4], get_sol().addTwoNumbers([0,1,1,2,4], [0,1,0,0,1]))
    def test2(self):
        self.assertEqual([0,2,1], get_sol().timeTaken([0,0,0], [1,0,1]))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):
