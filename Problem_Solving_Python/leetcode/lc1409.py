import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # bad solution
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        res = []
        li = [i for i in range(1,m+1)]
        for x in queries:
            idx = li.index(x)
            val = li[idx]
            res.append(idx)
            li.pop(idx)
            li = [val] + li
        return res


class MyTestCase(unittest.TestCase):
    def test1(self):
        queries,m = [3,1,2,1],  5
        Output= [2,1,2,1]
        self.assertEqual(Output, get_sol().processQueries(queries, m))
    def test2(self):
        queries,m = [4,1,2,2],  4
        Output= [3,1,2,0]
        self.assertEqual(Output, get_sol().processQueries(queries, m))
    def test3(self):
        queries,m = [7,5,5,8,3],  8
        Output= [6,5,0,7,5]
        self.assertEqual(Output, get_sol().processQueries(queries, m))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
