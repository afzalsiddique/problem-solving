import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))

class tester(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, get_sol().minPartitions('32'))
    def test_2(self):
        self.assertEqual(8, get_sol().minPartitions('82734'))
    def test_3(self):
        self.assertEqual(9, get_sol().minPartitions('27346209830709182346'))
