import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools;from sortedcontainers import SortedList
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD=10**9+7
        @functools.lru_cache(None)
        def recurse(n,k):
            if n==0:
                if k==0:
                    return 1
                return 0
            if k>n: return 0 # more sticks visible than sticks left       -- these two lines are essentially same
            # if k==n: return 1 # k=5,n=5 -> [1,2,3,4,5] only one option  -- these two lines are essentially same
            if k<0: return 0 # more than k sticks are visible

            res=0

            # choose tallest stick. Only one possibility because stick lengths are unique
            res+=recurse(n-1,k-1)
            res%=MOD

            # every stick except tallest stick. (n-1) possibility.
            res+=(n-1)*recurse(n-1,k)
            res%=MOD
            return res

        return recurse(n,k)
class Solution2:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD=10**9+7
        @functools.lru_cache(None)
        def recurse(n,k):
            if k==0: return 0 # no stick visible is not possible
            if k>n: return 0 # more sticks visible than sticks left
            if n==1: return 1 # first stick has to be visible

            res = 0

            # choose tallest stick. Only one possibility because stick lengths are unique
            res += recurse(n - 1, k - 1)
            res %= MOD

            # every stick except tallest stick. (n-1) possibility.
            res += (n-1) * recurse(n - 1, k)
            res %= MOD
            return res


        return recurse(n,k)


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(3,get_sol().rearrangeSticks(3,2))
    def test2(self):
        self.assertEqual(1,get_sol().rearrangeSticks(2,2))
    def test3(self):
        self.assertEqual(1,get_sol().rearrangeSticks(5,5))
    def test4(self):
        self.assertEqual(647427950,get_sol().rearrangeSticks(20, 11))
    def test5(self):
        self.assertEqual(3,get_sol().rearrangeSticks(3, 2))