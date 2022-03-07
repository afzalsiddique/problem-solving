import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(k): return MyCircularQueue(k)
class MyCircularQueue:
    def __init__(self, k: int):
        self.k=k
        self.begin=0
        self.end=-1
        self.li=[-1]*k
        self.left=k
    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.left-=1
        self.end=(self.end+1)%self.k
        self.li[self.end]=value
        return True
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.left+=1
        self.begin=(self.begin+1)%self.k
        return True
    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.li[self.begin]
    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.li[self.end]
    def isEmpty(self) -> bool:
        return self.left == self.k
    def isFull(self) -> bool:
        return self.left == 0
class MyCircularQueue2:
    def __init__(self, k: int):
        self.capacity=k
        self.left=k
        self.q=[-1]*k
        self.start=0
        self.end=-1
    def enQueue(self, value: int) -> bool:
        q=self.q
        if self.isFull():
            return False
        self.end+=1
        self.end%=self.capacity
        q[self.end]=value
        self.left-=1
        return True
    def deQueue(self) -> bool:
        q=self.q
        if self.isEmpty():
            return False
        q[self.start]=-1
        self.start+=1
        self.start%=self.capacity
        self.left+=1
        return True
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.start]
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.end]
    def isEmpty(self) -> bool:
        if self.left==self.capacity: return True
        return False
    def isFull(self) -> bool:
        if self.left: return False
        return True
    # def isEmpty(self) -> bool:
    #     if self.start==self.end and self.start==-1: return True
    #     return False
    # def isFull(self) -> bool:
    #     if self.start==self.end and self.start!=-1: return True
    #     return False
class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='MyCircularQueue':
                obj = get_sol(input[0])
                outputs.append(None)
            elif cmd=='enQueue':
                outputs.append(obj.enQueue(input[0]))
            elif cmd=='deQueue':
                outputs.append(obj.deQueue())
            elif cmd=='Front':
                outputs.append(obj.Front())
            elif cmd=='Rear':
                outputs.append(obj.Rear())
            elif cmd=='isFull':
                outputs.append(obj.isFull())
            elif cmd=='isEmpty':
                outputs.append(obj.isEmpty())
        return outputs
    def test01(self):
        commands = ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
        inputs=[       [3],             [1],         [2],      [3],        [4],      [],     [],       [],        [4],      []]
        exptected = [   None,           True,       True,     True,       False,     3,     True,     True,       True,     4]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(exptected,outputs)
    def test02(self):
        commands = ["MyCircularQueue","enQueue","enQueue","deQueue","enQueue","deQueue","enQueue","deQueue","enQueue","deQueue", "Front"]
        inputs=[[2],[1],[2],[],[3],[],[3],[],[3],[],[]]
        exptected = [None, True, True, True, True, True, True, True, True, True, 3]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(exptected,outputs)

