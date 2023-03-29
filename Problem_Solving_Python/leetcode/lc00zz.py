from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def dp(pos,steps):
            if steps==0:
                return pos==0
            if steps<pos: return 0
            res=0
            for s in range(1,steps+1):
                if pos+s>=arrLen:
                    break
                res+=dp(pos+s,steps-s)

            for s in range(1,steps+1):
                if pos-s<0:
                    break
                res+=dp(pos-s,steps-s)

            res+=dp(pos,steps-1)
            return res%(10**9+7)

        return dp(0,steps)


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(4,get_sol().numWays(steps = 3, arrLen = 2))
    def test2(self):
        self.assertEqual(2,get_sol().numWays(steps = 2, arrLen = 4))
    def test3(self):
        self.assertEqual(8,get_sol().numWays(steps = 4, arrLen = 2))
    def test4(self):
        self.assertEqual(9,get_sol().numWays(4, 3))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
