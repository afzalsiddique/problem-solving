from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List
import random


class RandomizedSet:
    def __init__(self):
        self.li = []
        self.di = {}

    def insert(self, val: int) -> bool:
        if val in self.di:return False
        self.di[val]=len(self.li)
        self.li.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.di:return False
        idx  = self.di[val]
        last=self.li[-1]
        self.li[idx]=last
        self.di[last]=idx
        self.li.pop()
        self.di.pop(val)
        return True
    def getRandom(self) -> int:
        return self.li[random.randint(0,len(self.li)-1)]
class mycase(unittest.TestCase):
    def test1(self):
        commands = ["RandomizedSet","remove","remove","insert","getRandom","remove","insert"]
        inputs = [[],[0],[0],[0],[],[0],[0]]
        outputs = []
        for c,i in zip(commands, inputs):
            if c == 'RandomizedSet':
                r = RandomizedSet()
            elif c =='insert':
                outputs.append(r.insert(i[0]))
            elif c=='remove':
                outputs.append(r.remove(i[0]))
            elif c=='getRandom':
                outputs.append(r.getRandom())
        exptected = [False,False,True,0,True,True]
        self.assertEqual(exptected,outputs)