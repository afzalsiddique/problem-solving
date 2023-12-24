from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list,ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        print(((-3)/2))
        print(int((-3) / 2))
        print(floor((-3) / 2))
        print(ceil((-3) / 2))


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([0,3,1,2,4], get_sol().maxNonDecreasingLength([0,1,1,2,4], [0,1,0,0,1]))
    def test2(self):
        self.assertEqual([0,2,1], get_sol().timeTaken([0,0,0], [1,0,1]))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):
