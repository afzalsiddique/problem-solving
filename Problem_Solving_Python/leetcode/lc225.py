from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return MyStack2()
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
    # using two queues
    def __init__(self):
        self.q1 = deque() # points to non-empty stack except when both stacks are empty
        self.q2 = deque() # points to empty stack

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1,self.q2=self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1)==0
class MyStack3:
    def __init__(self):
        self.q1=deque()
        self.q2=deque()
        self.q=self.q1
    def push(self, x: int) -> None:
        if not self.q1 and not self.q2:
            self.q.append(x)
            return
        if not self.q:
            self.q=self.q1 if self.q1 else self.q2
        self.q.append(x)
    def pop(self) -> int:
        emptyQ=self.q1 if not self.q1 else self.q2
        self.q=self.q1 if self.q1 else self.q2
        while self.q:
            tmp=self.q.popleft()
            if not self.q:
                return tmp
            emptyQ.append(tmp)
    def top(self) -> int:
        res=None
        emptyQ=self.q1 if not self.q1 else self.q2
        self.q=self.q1 if self.q1 else self.q2
        while self.q:
            res=self.q.popleft()
            emptyQ.append(res)
        return res
    def empty(self) -> bool:
        self.q=self.q1 if self.q1 else self.q2
        return bool(len(self.q)==0)
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
