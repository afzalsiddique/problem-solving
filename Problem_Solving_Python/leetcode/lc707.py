import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return MyLinkedList()

class Node:
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode
class MyLinkedList:

    def __init__(self):
        self.head = Node(0)  # Dummy node
        self.size = 0
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1

        cur = self.head
        for _ in range(index + 1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:  # Invalid index
            return

        prev = self.head
        for i in range(index):
            prev = prev.next

        # Add newNode between [prev] and [prev.next]
        newNode = Node(val, prev.next)
        prev.next = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:  # Invalid index
            return

        prev = self.head
        for i in range(index):
            prev = prev.next

        prev.next = prev.next.next
        self.size -= 1

class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='MyLinkedList':
                obj = get_sol(); outputs.append(None)
            elif cmd=='get':
                outputs.append(obj.get(input[0]))
            elif cmd=='addAtHead':
                outputs.append(obj.addAtHead(input[0]))
            elif cmd=='addAtTail':
                outputs.append(obj.addAtTail(input[0]))
            elif cmd=='addAtIndex':
                outputs.append(obj.addAtIndex(input[0],input[1]))
            elif cmd=='deleteAtIndex':
                outputs.append(obj.deleteAtIndex(input[0]))
        return outputs
    def test_01(self):
        commands = ["MyLinkedList","addAtHead","deleteAtIndex"]
        inputs=[      [],             [1],         [0]]
        expected = [None,             None,       None]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_02(self):
        commands = ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
        inputs=[        [],          [1],          [3],        [1, 2],      [1],      [1],           [1]]
        expected = [   None,         None,         None,       None,         2,      None,            3]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_03(self):
        commands = ["MyLinkedList","addAtIndex","addAtIndex","addAtIndex","get"]
        inputs=[    [],           [0,10],         [0,20],      [1,30],    [0]]
        expected = [None,         None,          None,         None,      20]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_04(self):
        commands = ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
        inputs=[      [],            [7],        [2],        [1],        [3,0],        [2],           [6],        [4],      [4],    [4],       [5,0],        [6]]
        expected = [None,None,None,None,None,None,None,None,                                                                 4,    None,        None,       None]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)

