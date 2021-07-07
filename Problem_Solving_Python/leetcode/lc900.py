import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(a): return RLEIterator(a)
class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.i=0
        self.li = encoding
    def next(self, n: int) -> int:
        li=self.li
        i=self.i
        while i<len(li) and li[i]<n:
            n-=li[i]
            li[i]=0
            i+=2
            self.i=i # because of "i=self.i"
        if i<len(li) and n<=li[i]:
            li[i]-=n
        if i==len(li): return -1
        return li[self.i+1]


class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='RLEIterator':
                obj = RLEIterator(input[0])
                outputs.append(None)
            elif cmd=='next':
                outputs.append(obj.next(input[0]))
        return outputs
    def test_01(self):
        commands = ["RLEIterator", "next", "next", "next", "next"]
        inputs=[[[3, 8, 0, 9, 2, 5]], [2], [1], [1], [2]]
        exptected = [None, 8, 8, 5, -1]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(exptected,outputs)
    def test_02(self):
        commands = ["RLEIterator","next","next","next","next","next","next","next","next","next","next"]
        inputs=[[[811,903,310,730,899,684,472,100,434,611]],[358],[345],[154],[265],[73],[220],[138],[4],[170],[88]]
        exptected = [None,                                   903,  903,  730,  684,  684,  684, 684, 684,  684, 684]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(exptected,outputs)

