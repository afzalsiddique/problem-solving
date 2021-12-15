import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/race-car/discuss/123834/JavaC++Python-DP-solution/122557
    def racecar(self, target: int) -> int:
        @functools.lru_cache(None)
        def func(i):
            n=i.bit_length()
            if 2**n-1==i:
                return n
            option2 = float('inf')
            option1 = n+1+func(2**n-1-i)
            for m in range(n-1):
                option2=min(option2, n+m+1+func(i-2**(n-1)+2**m))
            return min(option1,option2)

        return func(target)

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(2,Solution().racecar(3))
    def test2(self):
        self.assertEqual(5,Solution().racecar(6))
    def test3(self):
        self.assertEqual(39,Solution().racecar(6102))
    def test4(self):
        self.assertEqual(4,Solution().racecar(2))
    # def test5(self):