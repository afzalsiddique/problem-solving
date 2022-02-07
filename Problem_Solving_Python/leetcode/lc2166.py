from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(x): return Bitset(x)
class Bitset:
    def __init__(self, size: int):
        self.n=size
        self.allOne=2**size-1
        self.mask=0
        self.cnt=0
    def isOn(self,i:int):
        return (self.mask>>i)&1 # returns 1 when True or 0 when False
    def fix(self, i: int) -> None:
        i=self.n-i-1
        off=not self.isOn(i)
        mask=self.mask
        self.mask=mask|(1 << i)
        if off:
            self.cnt+=1
        # x=bin(self.mask)
        return
    def unfix(self, i: int) -> None:
        i=self.n-i-1
        on=self.isOn(i)
        mask=self.mask
        self.mask=mask&~(1 << i)
        if on:
            self.cnt-=1
        # x=bin(self.mask)
        return
    def flip(self) -> None:
        mask=self.mask
        self.mask=mask^self.allOne
        self.cnt=self.n-self.cnt
        # x=bin(self.mask)
        return
    def all(self) -> bool:
        return self.mask==self.allOne
    def one(self) -> bool:
        mask=self.mask
        return bool(mask&self.allOne)
    def count(self) -> int:
        return self.cnt
        # mask=self.mask
        # cnt = 0
        # while mask:
        #     cnt += 1
        #     mask = mask & (mask - 1)
        # return cnt
    def toString(self) -> str:
        tmp=bin(self.mask)[2:]
        # print(tmp)
        if len(tmp)<self.n:
            tmp='0'*(self.n-len(tmp))+tmp
        return tmp



class Tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='Bitset': obj = get_sol(input[0]); outputs.append(None)
            elif cmd=='fix': outputs.append(obj.fix(input[0]))
            elif cmd=='unfix': outputs.append(obj.unfix(input[0]))
            elif cmd=='flip': outputs.append(obj.flip())
            elif cmd=='all': outputs.append(obj.all())
            elif cmd=='one': outputs.append(obj.one())
            elif cmd=='count': outputs.append(obj.count())
            elif cmd=='toString': outputs.append(obj.toString())
        return outputs
    def test01(self):
        commands = ["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"]
        inputs=[[5], [3], [1], [], [], [0], [], [], [0], [], []]
        expected = [None, None, None, None, False, None, None, True, None, 2, "01010"]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test02(self):
        commands = ["Bitset","flip","unfix","all","fix","fix","unfix","all","count","toString","toString","toString","unfix","flip","all","unfix","one","one",  "all","fix","unfix"]
        inputs=[    [2],       [],  [1],    [],   [1],   [1],  [1],   [],     [],     [],        [],        [],       [0],    [],    [],   [0],     [],  [],  [],    [0],   [0]]
        expected = [None,    None,   None,  False,None, None, None,   False,  1,    "10",       "10",      "10",      None,  None,   True, None,   True,True,  False, None,  None]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)

