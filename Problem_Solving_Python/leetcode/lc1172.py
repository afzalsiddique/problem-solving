import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
# from ..template.binary_tree import deserialize,serialize
def get_sol(x): return DinnerPlates(x)
class DinnerPlates:
    # Min Heap pops out index of the leftmost stack
    # Use a heap to record all the popAtStack- index. Insert at these locations first. If the heap is empty, (that means all the stacks except the last one are full) then insert at the end of the stacks.
    # video note
    def __repr__(self): return '\n'.join([str(st) for st in self.st])
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.st=[[] for _ in range(2*10**5+1)]
        self.right=0
        self.pq=[]
    def updateHeap(self):
        pq=self.pq
        while pq and pq[0]>=self.right:
            heappop(pq)
        return
    def updateRightPointer(self):
        while self.right>0 and not self.st[self.right]:
            self.right-=1
        return
    def push(self, val: int) -> None:
        self.updateHeap()
        if self.pq: # insert at free spaces in between
            stack_idx=heappop(self.pq)
            self.st[stack_idx].append(val)
            return
         # insert at the very last
        if len(self.st[self.right])==self.capacity:
            self.right+=1
        self.st[self.right].append(val)
        return
    def pop(self) -> int:
        self.updateRightPointer()
        tmpStack=self.st[self.right]
        if len(tmpStack)==0: return -1
        return tmpStack.pop()
    def popAtStack(self, index: int) -> int:
        self.updateRightPointer()
        # if index==self.right: return self.pop() # not required
        tmpStack=self.st[index]
        if len(tmpStack)==0: return -1
        heappush(self.pq,index)
        return self.st[index].pop()

class DinnerPlates2:
    # Use a heap to record all the popAtStack- index. Insert at these locations first. If the heap is empty, (that means all the stacks except the last one are full) then insert at the end of the stacks.
    def __init__(self, capacity: int):
        self.c=capacity
        self.stacks=[]
        self.pq=[]
    def push(self, val: int) -> None:
        stacks,pq=self.stacks,self.pq
        while self.pq and pq[0]<len(stacks) and len(stacks[pq[0]])==self.c: # remove irrelevant stack index from pq
            heappop(pq)
        if self.pq and self.pq[0]<len(stacks):
            stacks[pq[0]].append(val)
            return
        if not stacks:
            stacks.append([])
        if len(stacks[-1])==self.c:
            stacks.append([])
        stacks[-1].append(val)
        return
    def pop(self) -> int:
        stacks,pq=self.stacks,self.pq
        while stacks and not stacks[-1]:
            stacks.pop()
        return self.popAtStack(len(stacks)-1)
    def popAtStack(self, index: int) -> int:
        stacks,pq=self.stacks,self.pq
        if 0<=index<len(stacks) and stacks[index]:
            heappush(pq,index)
            return stacks[index].pop()
        return -1


class MyTese(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            # print(i)
            # print(obj,end='\n')
            if i==12:
                a='b'
            if cmd=='DinnerPlates':
                obj = get_sol(input[0])
                outputs.append(None)
            elif cmd=='push':
                outputs.append(obj.push(input[0]))
            elif cmd=='pop':
                outputs.append(obj.pop())
            elif cmd=='popAtStack':
                outputs.append(obj.popAtStack(input[0]))
        return outputs
    def test01(self):
        commands = ["DinnerPlates", "push", "push", "pop", "pop", "pop"]
        inputs=[       [2],         [1],     [2],    [],    [],    [] ]
        expected = [None,           None,   None,     2,     1,    -1 ]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test02(self):
        commands = ["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop"]
        inputs=[       [2],         [1],     [2],    [3],    [4],    [5],     [0],         [20],   [21],      [0],         [2],        [],     [],   [],     [],    []]
        expected = [None,           None,   None,     None,  None,    None,     2,          None,  None,      20,          21,          5,      4,    3,       1,    -1]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test03(self):
        commands = ["DinnerPlates","push","push","popAtStack","pop","push","push","pop","pop"]
        inputs=[       [1],        [1],    [2],   [1],         [],   [1],   [2],   [],   []]
        expected = [None,         None,    None,   2,          1,   None,   None,   2,    1]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test04(self):
        commands = ["DinnerPlates","push","push","push","push","push","push","push","push","popAtStack","popAtStack","popAtStack","popAtStack"]
        inputs=[      [2],         [1],     [2],   [3],  [4],   [5],    [6],  [7],   [8],     [3],         [3],         [1],          [3],     ]
        expected = [None,         None,    None,  None,   None, None,  None,  None,   None,     8,          7,           4,           -1]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test05(self):
        commands = ["DinnerPlates","push","push","push","push","push","push","push","push","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","push","push","push","push","push","push","push","push","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop"]
        inputs=[      [2],         [472],  [106], [497],[498],  [73],  [115], [437], [461],  [3],         [3],         [1],          [3],         [0],        [2],[2],[1],[1],[3],[197],[239],[129],[449],[460],[240],[386],[343],[],[],[],[],[],[],[],[],[],[]]
        expected = [None,           None,   None,  None, None,  None,  None,  None,  None,   461,       437,           498,           -1,         106,115,73,497,-1,-1,None,None,None,None,None,None,None,None,343,386,240,460,449,129,239,197,472,-1]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test06(self):
        commands = ["DinnerPlates","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop"]
        inputs=[[2],[373],[86],[395],[306],[370],[94],[41],[17],[387],[403],[66],[82],[27],[335],[252],[6],[269],[231],[35],[346],[4],[6],[2],[5],[2],[2],[7],[9],[8],[1],[474],[216],[256],[196],[332],[43],[75],[22],[273],[101],[11],[403],[33],[365],[338],[331],[134],[1],[250],[19],[],[],[],[],[],[],[],[],[],[]]
        expected = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 403, 335, 94, 82, 370, -1, 6, 346, 231, 306, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 19, 250, 1, 134, 331, 338, 365, 33, 403, 11]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)


