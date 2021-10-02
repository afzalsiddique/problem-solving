import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        res=0
        x = n//2
        while x!=1:
            if x%2:
                x = n//2 + (x-1)//2
            else:
                x = x//2
            res+=1
        return res+1


class MyTestCase(unittest.TestCase):
    def test_1(self):
        n,Output = 2, 1
        self.assertEqual(Output, get_sol().reinitializePermutation(n))
    def test_2(self):
        n,Output = 4, 2
        self.assertEqual(Output, get_sol().reinitializePermutation(n))
    def test_3(self):
        n,Output = 6, 4
        self.assertEqual(Output, get_sol().reinitializePermutation(n))
    def test_4(self):
        n,Output = 8, 3
        self.assertEqual(Output, get_sol().reinitializePermutation(n))
    def test_5(self):
        n,Output = 10, 6
        self.assertEqual(Output, get_sol().reinitializePermutation(n))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):