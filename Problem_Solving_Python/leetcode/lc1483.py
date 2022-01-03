import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
# from ..template.binary_tree import deserialize,serialize
def get_sol(x,y): return TreeAncestor(x,y)
class TreeAncestor:
    # https://www.youtube.com/watch?v=oib-XsjFa-M
    # binary lifting
    def __init__(self, n: int, parent: List[int]):
        self.LOG=20
        up=[[-1]*self.LOG for _ in range(n)]
        for node in range(n):
            up[node][0]=parent[node] # 2**0 th (2**0=1, 1st) ancestor of node is parent node

        for i in range(1,20): # find the ith ancestor
            for node in range(n): # of node
                ancestor = up[node][i-1]
                if ancestor!=-1:
                    up[node][i]=up[ancestor][i-1]
        self.up=up
    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self.LOG):
            if k & (1<<i):
                node=self.up[node][i]
                if node==-1:
                    return -1
        return node


class Tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='TreeAncestor':
                obj = get_sol(input[0],input[1])
                outputs.append(None)
            elif cmd=='getKthAncestor':
                outputs.append(obj.getKthAncestor(input[0],input[1]))
        return outputs
    def test_01(self):
        commands = ["TreeAncestor",       "getKthAncestor", "getKthAncestor", "getKthAncestor"]
        inputs=[[7, [-1, 0, 0, 1, 1, 2, 2]], [3, 1],          [5, 2],           [6, 3]]
        expected = [None,                     1,               0,                -1]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_02(self):
        commands = ["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
        inputs=[[5,[-1,0,0,1,2]],[3,5],[3,2],[2,2],[0,2],[2,1]]
        expected = [None,-1,0,-1,-1,0]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_03(self):
        commands = ["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
        inputs=[[4,[-1,2,3,0]],[2,3],[2,2],[2,1]]
        expected = [None,-1,0,3]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
