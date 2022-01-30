import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = {}
        def helper(n, target):
            if n==0:
                if target==0: return 1
                else: return 0
            if target<0: return 0
            if (n, target) in dp: return dp[(n, target)]
            total=0
            for i in range(1, k + 1):
                total+=helper(n - 1, target - i)
            dp[(n, target)]= total % 1_000_000_007
            return dp[(n, target)]

        return helper(n, target)

class tester(unittest.TestCase):
    def test_1(self):
        d = 1
        f = 6
        target = 3
        Output= 1
        self.assertEqual(Output, get_sol().numRollsToTarget(d,f,target))
    def test_2(self):
        d = 2
        f = 6
        target = 7
        Output= 6
        self.assertEqual(Output, get_sol().numRollsToTarget(d,f,target))
    def test_3(self):
        d = 2
        f = 5
        target = 10
        Output= 1
        self.assertEqual(Output, get_sol().numRollsToTarget(d,f,target))
    def test_4(self):
        d = 1
        f = 2
        target = 3
        Output= 0
        self.assertEqual(Output, get_sol().numRollsToTarget(d,f,target))
    def test_5(self):
        d = 30
        f = 30
        target = 500
        Output= 222616187
        self.assertEqual(Output, get_sol().numRollsToTarget(d,f,target))
