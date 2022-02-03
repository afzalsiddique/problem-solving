from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return MyStack()
class MyStack:
    # using one queue
    def __init__(self):
        self._queue = deque()

    def push(self, x):
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]

    def empty(self):
        return not len(self._queue)
class MyStack2:
    # using one queue
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1,self.q2=self.q2, self.q1

    def pop(self) -> int:
        return self.q1.pop(0)

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        if not self.q1:return True
        return False
class Tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='MyStack': obj = get_sol(); outputs.append(None)
            elif cmd=='push': outputs.append(obj.push(input[0]))
            elif cmd=='pop': outputs.append(obj.pop())
            elif cmd=='top': outputs.append(obj.top())
            elif cmd=='empty': outputs.append(obj.empty())
        return outputs
    def test01(self):
        commands = ["MyStack", "push", "push", "top", "pop", "empty"]
        inputs=[[], [1], [2], [], [], []]
        expected = [None, None, None, 2, 2, False]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
