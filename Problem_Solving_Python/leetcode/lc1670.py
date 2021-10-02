import heapq; import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return FrontMiddleBackQueue()
class FrontMiddleBackQueue:
    def __init__(self):
        self.first = deque()
        self.second = deque()
    def balance(self): # second list should equal or greater than first in length
        first,second = self.first, self.second
        if len(second)-len(first)>1:
            first.append(second.popleft())
        elif len(first)>len(second):
            second.appendleft(first.pop())
    def pushFront(self, val: int) -> None:
        self.first.appendleft(val)
        self.balance()
        return None
    def pushMiddle(self, val: int) -> None:
        self.first.append(val)
        self.balance()
        return None
    def pushBack(self, val: int) -> None:
        self.second.append(val)
        self.balance()
        return None
    def popFront(self) -> int:
        first,second = self.first, self.second
        if first:
            ans=first.popleft()
        elif second:
            ans = second.popleft()
        else:
            ans=-1
        self.balance()
        return ans
    def popMiddle(self) -> int:
        first,second = self.first, self.second
        if len(second)>len(first):
            ans=second.popleft()
        elif first:
            ans = first.pop()
        else:
            ans=-1
        self.balance()
        return ans
    def popBack(self) -> int:
        second=self.second
        if second:
            ans = self.second.pop()
        else:
            ans=-1
        self.balance()
        return ans
class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='FrontMiddleBackQueue':
                obj = get_sol()
                outputs.append(None)
            elif cmd=='pushFront':
                outputs.append(obj.pushFront(input[0]))
            elif cmd=='pushMiddle':
                outputs.append(obj.pushMiddle(input[0]))
            elif cmd=='pushBack':
                outputs.append(obj.pushBack(input[0]))
            elif cmd=='popFront':
                outputs.append(obj.popFront())
            elif cmd=='popMiddle':
                outputs.append(obj.popMiddle())
            elif cmd=='popBack':
                outputs.append(obj.popBack())
        return outputs
    def test_01(self):
        commands = ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
        inputs=[[], [1], [2], [3], [4], [], [], [], [], []]
        expected = [None, None, None, None, None, 1, 3, 4, 2, -1]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_02(self):
        commands = ["FrontMiddleBackQueue","pushFront","pushFront","pushFront","pushFront","popBack","popBack","popBack","popBack"]
        inputs=[[],[1],[2],[3],[4],[],[],[],[]]
        expected = [None,None,None,None,None,1,2,3,4]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_03(self):
        commands = ["FrontMiddleBackQueue","pushMiddle","pushMiddle","pushMiddle","popMiddle","popMiddle","popMiddle"]
        inputs=[[],[1],[2],[3],[],[],[]]
        expected = [None, None, None, None, 3, 2, 1]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_04(self):
        commands = ["FrontMiddleBackQueue","popMiddle","popMiddle","pushMiddle","popBack","popFront","popMiddle"]
        inputs=[[],[],[],[8],[],[],[]]
        expected = [None,-1,-1,None,8,-1,-1]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_05(self):
        commands = ["FrontMiddleBackQueue","pushFront","pushMiddle","pushMiddle","pushFront","pushFront","pushMiddle","popMiddle","popMiddle","pushMiddle","pushMiddle","popFront"]
        inputs=[[],[1],[2],[3],[4],[5],[6],[],[],[7],[8],[]]
        expected = [None,None,None,None,None,None,None,6,2,None,None,5]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)

