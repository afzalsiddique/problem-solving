import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/discuss/1403913/Python-math-oneliner-with-proof-explained
    def minNonZeroProduct(self, p: int) -> int:
        MOD=10**9+7
        base = pow(2,p)-2
        power=pow(2,p-1)-1
        last=pow(2,p)-1
        return (pow(base,power,MOD)*last)%MOD


class MyTestCase(unittest.TestCase):
    def test_1(self):
        p = 1
        Output= 1
        self.assertEqual(Output, get_sol().minNonZeroProduct(p))
    def test_2(self):
        p = 2
        Output= 6
        self.assertEqual(Output, get_sol().minNonZeroProduct(p))
    def test_3(self):
        p = 3
        Output= 1512
        self.assertEqual(Output, get_sol().minNonZeroProduct(p))
    def test_4(self):
        p = 4
        Output= 581202553
        self.assertEqual(Output, get_sol().minNonZeroProduct(p))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):