import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    # wrong
    def flipLights(self, n: int, presses: int) -> int:
        def flip(state,i):
            return state ^ (1<<i)
        def button1(state):
            for i in range(n):
                state = flip(state,i)
            return state
        def button2(state): # even. index starts from 0. so flip odd.
            for i in range(1,n,2):
                state = flip(state,i)
            return state
        def button3(state): # odd. index starts from 0. so flip even.
            for i in range(0,n,2):
                state = flip(state,i)
            return state
        def button4(state):
            for i in range(0,n,3):
                state = flip(state,i)
            return state
        def func(state,presses):
            if presses==0:
                vis.add(state)
                return
            if state in vis:
                return
            states = [button1(state),button2(state),button3(state),button4(state)]
            for s in states:
                vis.add(s)
                func(s,presses-1)
            return

        state = 2**n-1
        vis = set()
        func(state,presses)
        return len(vis)


class MyTestCase(unittest.TestCase):
    def test1(self):
        n,presses = 1,  1
        Output= 2
        self.assertEqual(Output, get_sol().flipLights(n,presses))
    def test2(self):
        n,presses = 2,  1
        Output= 3
        self.assertEqual(Output, get_sol().flipLights(n,presses))
    def test3(self):
        n,presses = 3,  1
        Output= 4
        self.assertEqual(Output, get_sol().flipLights(n,presses))
    def test4(self):
        n,presses = 1,  0
        Output= 1
        self.assertEqual(Output, get_sol().flipLights(n,presses))
    def test5(self):
        n,presses = 1,  2
        Output= 2
        self.assertEqual(Output, get_sol().flipLights(n,presses))
    def test6(self):
        n,presses = 2, 2
        Output= 4
        self.assertEqual(Output, get_sol().flipLights(n,presses))
    # def test7(self):
