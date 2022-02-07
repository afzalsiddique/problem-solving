from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return MyQueue()
class MyQueue:
    def __init__(self):
        self.s1=[] # non-empty stack except when both stacks are empty
        self.s2=[] # empty stack
    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
        return
    def pop(self) -> int:
        return self.s1.pop()
    def peek(self) -> int:
        return self.s1[-1]
    def empty(self) -> bool:
        return not bool(self.s1)

class MyQueue2:
    def __init__(self):
        self.push_stack=[]
        self.pop_stack=[]

    def push(self, x: int) -> None:
        self.push_stack.append(x)
    def pop(self) -> int:
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()
    def peek(self) -> int:
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]
    def empty(self) -> bool:
        if not self.push_stack and not self.pop_stack:return True
        return False




class Tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='MyQueue': obj = get_sol(); outputs.append(None)
            elif cmd=='push': outputs.append(obj.push(input[0]))
            elif cmd=='pop': outputs.append(obj.pop())
            elif cmd=='peek': outputs.append(obj.peek())
            elif cmd=='empty': outputs.append(obj.empty())
        return outputs
    def test01(self):
        commands = ["MyQueue", "push", "push", "peek", "pop", "empty"]
        inputs=[[], [1], [2], [], [], []]
        expected = [None, None, None, 1, 1, False]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
