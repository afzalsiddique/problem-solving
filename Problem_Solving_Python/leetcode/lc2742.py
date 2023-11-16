from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union, Dict; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list, ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize

def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=qMZJunF5UaI
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @cache
        def recur(i,remain):
            if remain<=0:
                return 0
            if i==n:
                return float('inf')
            paint=cost[i]+recur(i+1,remain-1-time[i])
            skip=recur(i+1,remain)
            return min(paint,skip)

        n=len(cost)
        return recur(0,n)


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(3,get_sol().paintWalls( [1,2,3,2], [1,2,3,2]))
    def test02(self):
        self.assertEqual(4,get_sol().paintWalls([2,3,4,2],  [1,1,1,1]))
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
