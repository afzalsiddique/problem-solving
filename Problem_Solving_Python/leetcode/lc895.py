import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return FreqStack()
class FreqStack:
    def __init__(self):
        self.freq=[[] for _ in range(20000)]
        self.count=Counter()
        self.maxx=0
    def push(self, val: int) -> None:
        prev=self.count[val]
        self.count[val]+=1
        self.freq[prev+1].append(val)
        self.maxx=max(self.maxx,prev+1)
    def pop(self) -> int:
        res = self.freq[self.maxx].pop()
        self.count[res]-=1
        if not self.freq[self.maxx]:
            self.maxx-=1
        return res
class FreqStack2:
    def __init__(self):
        self.pq=[]
        self.i=1
        self.count=Counter()
    def push(self, val: int) -> None:
        self.count[val]+=1
        heappush(self.pq,(-self.count[val],-self.i,val))
        self.i+=1
    def pop(self) -> int:
        freq,idx,val=heappop(self.pq)
        self.count[val]-=1
        return val

class Tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='FreqStack':
                obj = get_sol()
                outputs.append(None)
            elif cmd=='push':
                outputs.append(obj.push(input[0]))
            elif cmd=='pop':
                outputs.append(obj.pop())
        return outputs
    def test01(self):
        commands = ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
        inputs=[[],              [5],     [7],     [5],    [7],    [4],   [5],    [],    [],    [],    []]
        expected = [None,        None,    None,    None,   None,  None,   None,   5,      7,    5,     4]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test02(self):
        commands = ["FreqStack","push","push","push","push","push","push","pop","push","pop","push","pop","push","pop","push","pop","pop","pop","pop","pop","pop"]
        inputs=[      [],       [4],    [0],   [9],   [3],   [4],    [2],   [],  [6],   [],   [1],   [],   [1],    [],  [4],   [],   [],   [],    [],  [],   []]
        expected = [None,      None,   None,    None, None,  None,  None,   4,   None,  6,   None,   1,    None,  1,   None,   4,     2,    3,     9,   0,    4]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test03(self):
        commands = ["FreqStack","push","push","push","push","pop", "pop", "push", "push", "push", "pop", "pop", "pop"]
        inputs=[     [],          [1],  [1],   [1],   [2],   [],     [],   [2],     [2],    [1],    [],   [],   []]
        expected = [None,        None,   None,None,  None,    1,     1,   None,    None,   None,     2,   1,     2]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
