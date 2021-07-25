import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        li = []
        for ch in s:
            li.append(str(ord(ch)-96))
        li=''.join(li)
        for _ in range(k):
            li = [int(x) for x in li]
            li=sum(li)
            li=str(li)
        return int(li)

class tester(unittest.TestCase):
    def test_1(self):
        s = "iiii"
        k = 1
        Output= 36
        self.assertEqual(Output, get_sol().getLucky(s,k))
    def test_2(self):
        s = "leetcode"
        k = 2
        Output= 6
        self.assertEqual(Output, get_sol().getLucky(s,k))
    def test_3(self):
        s = "zbax"
        k = 2
        Output= 8
        self.assertEqual(Output, get_sol().getLucky(s,k))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
