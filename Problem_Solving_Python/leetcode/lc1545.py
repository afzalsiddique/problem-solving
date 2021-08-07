import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        n-=1
        k-=1
        def get_next(li):
            li.extend([1]+list(reversed([x^1 for x in li])))
            return li

        li=[0]
        for i in range(n):
            li=get_next(li)
        return str(li[k])

class Tester(unittest.TestCase):
    def test_1(self):
        n,k = 3,1
        Output= "0"
        self.assertEqual(Output,get_sol().findKthBit(n,k))
    def test_2(self):
        n,k = 4,11
        Output= "1"
        self.assertEqual(Output,get_sol().findKthBit(n,k))
    def test_3(self):
        n,k = 1,1
        Output= "0"
        self.assertEqual(Output,get_sol().findKthBit(n,k))
    def test_4(self):
        n,k = 2,3
        Output= "1"
        self.assertEqual(Output,get_sol().findKthBit(n,k))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
