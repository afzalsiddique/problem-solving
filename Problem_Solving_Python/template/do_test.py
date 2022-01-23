import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
import heapq
def get_sol(): return MyQueue()


class MyQueue:

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
    def test_01(self):
        commands = ["MyQueue","push","push","push","push","pop","push","pop","pop","pop","pop"]
        inputs=[      [],       [1],   [2],  [3],    [4],  [],   [5],    [],   [],  [],   []]
        expected = [None,None,None,None,None,1,None,2,3,4,5]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_02(self):
        commands = ["MyQueue", "push", "push", "peek", "pop", "empty"]
        inputs =  [[], [1], [2], [], [], []]
        expected = [None, None, None, 1, 1, False]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
