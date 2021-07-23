import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(k): return MyCircularDeque(k)
class MyCircularDeque:
    def __init__(self, k: int):
        self.capacity = k
        self.left=k

        self.start=1
        self.end=0
        # also works
        self.start=0
        self.end=-1

        self.q=[-1]*k
    def insertFront(self, value: int) -> bool:
        q=self.q
        if self.isFull(): return False
        self.start-=1
        self.start%=self.capacity
        q[self.start]=value
        self.left-=1
        return True
    def insertLast(self, value: int) -> bool:
        q=self.q
        if self.isFull():
            return False
        self.end+=1
        self.end%=self.capacity
        q[self.end]=value
        self.left-=1
        return True
    def deleteFront(self) -> bool:
        q=self.q
        if self.isEmpty():
            return False
        q[self.start]=-1
        self.start+=1
        self.start%=self.capacity
        self.left+=1
        return True
    def deleteLast(self) -> bool:
        q=self.q
        if self.isEmpty():
            return False
        q[self.end]=-1
        self.end-=1
        self.end%=self.capacity
        self.left+=1
        return True
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.start]
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.end]
    def isEmpty(self) -> bool:
        if self.left==self.capacity: return True
        return False
    def isFull(self) -> bool:
        if self.left: return False
        return True
class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='MyCircularDeque':
                obj = get_sol(input[0])
                outputs.append(None)
            elif cmd=='insertFront':
                outputs.append(obj.insertFront(input[0]))
            elif cmd=='insertLast':
                outputs.append(obj.insertLast(input[0]))
            elif cmd=='getFront':
                outputs.append(obj.getFront())
            elif cmd=='getRear':
                outputs.append(obj.getRear())
            elif cmd=='deleteFront':
                outputs.append(obj.deleteFront())
            elif cmd=='deleteLast':
                outputs.append(obj.deleteLast())
            elif cmd=='isFull':
                outputs.append(obj.isFull())
            elif cmd=='isEmpty':
                outputs.append(obj.isEmpty())
        return outputs
    def test_01(self):
        commands = ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
        inputs=[[3], [1], [2], [3], [4], [], [], [], [4], []]
        exptected = [None, True, True, True, False, 2, True, True, True, 4]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(exptected,outputs)
    def test_02(self):
        commands = ["MyCircularDeque","insertFront","insertLast","getFront","insertLast","getFront","insertFront","getRear","getFront","getFront","deleteLast","getRear"]
        inputs=[       [5],              [7],          [0],         [],        [3],        [],          [9],         [],       [],         [],        [],        []]
        exptected = [None,              True,          True,        7,        True,        7,          True,           3,      9,          9,         True,      0]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(exptected,outputs)


