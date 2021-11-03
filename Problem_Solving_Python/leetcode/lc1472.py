import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(x): return BrowserHistory(x)
class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur = homepage
        self.b = []
        self.f = deque()
    def visit(self, url: str) -> None:
        self.f=deque()
        self.b.append(self.cur)
        self.cur=url
    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.b:
                self.f.appendleft(self.cur)
                self.cur = self.b.pop()
            else: # if back not available
                break
        return self.cur

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.f:
                self.b.append(self.cur)
                self.cur = self.f.popleft()
            else: # if forward not available
                break
        return self.cur

class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='BrowserHistory':
                obj = get_sol(input[0])
                outputs.append(None)
            elif cmd=='visit':
                outputs.append(obj.visit(input[0]))
            elif cmd=='back':
                outputs.append(obj.back(input[0]))
            elif cmd=='forward':
                outputs.append(obj.forward(input[0]))
        return outputs

    def test_01(self):
        commands = ["BrowserHistory","visit",         "visit",          "visit",     "back","back","forward",    "visit",    "forward","back","back"]
        inputs=[   ["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],  [1],   [1],    [1],   ["linkedin.com"],   [2],    [2],   [7]]
        expected = [None,None,None,None,"facebook.com","google.com","facebook.com",None,"linkedin.com","google.com","leetcode.com"]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
