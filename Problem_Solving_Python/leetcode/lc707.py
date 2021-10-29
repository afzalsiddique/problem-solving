import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return MyLinkedList()

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next=next
    def __repr__(self): return str(self.val) + "->" + str(self.next)
class MyLinkedList:
    def __init__(self):
        self.dummy_tail = Node(-1)
        self.dummy_head = Node(-1,self.dummy_tail)
        self.n=0
    def _get_node(self,index):
        if index>=self.n: return None
        if index==-1: return self.dummy_head
        cur = self.dummy_head
        while index:
            cur = cur.next
            index-=1
        return cur.next
    def get(self, index: int) -> int:
        node = self._get_node(index)
        if node: return node.val
        return -1

    def _add_after(self, val, node):
        next = node.next
        node.next = Node(val, next)
        self.n+=1
    def addAtHead(self, val: int) -> None:
        self._add_after(val,self.dummy_head)

    def addAtTail(self, val: int) -> None:
        node = self._get_node(self.n-1)
        self._add_after(val,node)

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.n: return None
        node = self._get_node(index-1)
        self._add_after(val,node)

    def deleteAtIndex(self, index: int) -> None:
        if index>=self.n: return None
        self.n-=1
        node = self._get_node(index-1)
        node.next = node.next.next

class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='MyLinkedList':
                obj = get_sol()
                outputs.append(None)
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

