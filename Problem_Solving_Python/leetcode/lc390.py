import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def lastRemaining(self, n: int) -> int:
        remain = n
        head = 1
        steps = 1
        left = True
        while remain>1:
            if left:
                head += steps
            else:
                if remain%2:
                    head+=steps
            steps*=2
            left=not left
            remain//=2
        return head

class MyTestCase(unittest.TestCase):
    def test1(self):
        n = 9
        Output= 6
        self.assertEqual(Output, get_sol().lastRemaining(n))
    def test2(self):
        n = 1
        Output= 1
        self.assertEqual(Output, get_sol().lastRemaining(n))
    # def test3(self):
    # def test4(self):
    # def test5(self):
