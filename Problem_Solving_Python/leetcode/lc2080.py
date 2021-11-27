import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(x): return RangeFreqQuery(x)

class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.di=defaultdict(list)
        for i,x in enumerate(arr):
            self.di[x].append(i)
    def query(self, left: int, right: int, value: int) -> int:
        l_idx=bisect_left(self.di[value],left)
        r_idx=bisect_right(self.di[value],right)
        return r_idx-l_idx




class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='RangeFreqQuery':
                obj = get_sol(input[0])
                outputs.append(None)
            elif cmd=='query':
                outputs.append(obj.query(input[0],input[1],input[2]))
        return outputs
    def test_01(self):
        commands = ["RangeFreqQuery", "query", "query"]
        inputs=[[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
        expected = [None, 1, 2]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
