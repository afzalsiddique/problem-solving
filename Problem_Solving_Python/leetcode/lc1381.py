import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(maxSize): CustomStack(maxSize)
class CustomStack:
    # time O(1) for each operation
    # space O(maxsize)
    # https://leetcode.com/problems/design-a-stack-with-increment-operation/discuss/539716/JavaC%2B%2BPython-Lazy-increment-O(1)
    def __init__(self, maxSize: int):
        self.remain=maxSize
        self.increase = []
        self.st=[]
    def push(self, x: int) -> None:
        if not self.remain: return
        self.st.append(x)
        self.increase.append(0)
        self.remain-=1
    def pop(self) -> int:
        if not self.st: return -1
        self.remain+=1
        if len(self.increase)==1:
            return self.st.pop()+self.increase.pop()
        tmp=self.increase[-1]
        self.increase[-2]+=self.increase[-1]
        self.increase.pop()
        return tmp+self.st.pop()
    def increment(self, k: int, val: int) -> None:
        if not self.st: return
        idx = min(k,len(self.st))
        self.increase[idx-1]+=val

class CustomStack2:
    def __init__(self, maxSize: int):
        self.remain=maxSize
        self.st=[]
        self.li=[0]*maxSize
    def push(self, x: int) -> None:
        if self.remain:
            self.st.append(x)
            self.remain-=1
    def pop(self) -> int:
        if not self.st: return -1
        idx=len(self.st)-1
        tmp=self.li[idx]
        self.li[idx]=0
        self.remain+=1
        return self.st.pop()+tmp
    def increment(self, k: int, val: int) -> None:
        n=len(self.st)
        for i in range(min(k,n)):
            self.li[i]+=val

class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='CustomStack':
                obj = CustomStack(input[0])
                outputs.append(None)
            elif cmd=='push':
                outputs.append(obj.push(input[0]))
            elif cmd=='pop':
                outputs.append(obj.pop())
            elif cmd=='increment':
                outputs.append(obj.increment(input[0],input[1]))
        return outputs
    def test_1(self):
        commands = ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
        inputs=[          [3],      [1],  [2],   [],   [2],   [3],    [4],   [5,100],    [2,100],   [],    [],  [],   []]
        out_exptected = [None,None,None,2,None,None,None,None,None,103,202,201,-1]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(out_exptected,outputs)
    def test_2(self):
        commands = ["CustomStack","push","pop","increment","pop","increment","push","pop","push","increment","increment","increment"]
        inputs=[           [2],    [34],  [],   [8,100],    [],     [9,91],   [63],  [],   [84],   [10,93],     [6,45],    [10,4]]
        out_exptected = [ None,   None,   34,   None,      -1,       None,    None,  63,   None,   None,         None,      None]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(out_exptected,outputs)

