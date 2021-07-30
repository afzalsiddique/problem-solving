import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        di = defaultdict(set)
        for u,v in edges:
            di[u].add(v)
            di[v].add(u)
        n=len(di)
        for node in di:
            if len(di[node])==n-1:
                return node

class MyTestCase(unittest.TestCase):
    def test_1(self):
        actual =get_sol().findCenter([[1,2],[2,3],[4,2]])
        expected = 2
        self.assertEqual(expected, actual)
    def test_2(self):
        actual =get_sol().findCenter([[1,2],[5,1],[1,3],[1,4]])
        expected = 1
        self.assertEqual(expected, actual)
