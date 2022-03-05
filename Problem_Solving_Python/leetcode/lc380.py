from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return RandomizedSet()

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
class Tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='RandomizedSet': obj = get_sol(); outputs.append(None)
            elif cmd=='insert': outputs.append(obj.insert(input[0]))
            elif cmd=='remove': outputs.append(obj.remove(input[0]))
            elif cmd=='getRandom': outputs.append(obj.getRandom())
        return outputs
    def test01(self):
        commands = ["RandomizedSet","remove","remove","insert","getRandom","remove","insert"]
        inputs=[[],[0],[0],[0],[],[0],[0]]
        expected = [None,False,False,True,0,True,True]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
