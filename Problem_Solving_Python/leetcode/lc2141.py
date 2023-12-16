from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union, Dict; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list, ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize

def get_sol(): return Solution()
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def ifPossible(x):
            # If a battery has more than x charge. This extra charge is useless.
            # because we need to run all the computers simultaneously.
            # So for each battery with charge > x, it can only power 1 computer

            # For other batteries,
            # Sum up the charges and check if they can provide power to the rest of the computers
            BatteriesEqualOrGreaterThanX=sum(1 for b in batteries if b>=x)
            if BatteriesEqualOrGreaterThanX>=n: return True
            otherComputers=n-BatteriesEqualOrGreaterThanX
            sumLessThanX=sum(b for b in batteries if b<x)
            return sumLessThanX>=x*otherComputers

        lo,hi=0,sum(batteries)+1
        while lo<=hi:
            m=(lo+hi)//2
            if ifPossible(m):
                lo=m+1
            else:
                hi=m-1
        return lo-1



class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(4, get_sol().maxRunTime(2, [3,3,3]))
    def test2(self):
        self.assertEqual(2, get_sol().maxRunTime(2, [1,1,1,1]))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
