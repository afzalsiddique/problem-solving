import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Skiplist()
class Node:
    def __init__(self,val:int,next,down):
        self.val=val
        self.next=next
        self.down=down
    def __repr__(self):
        return str(self.val)
class Skiplist:
    def __init__(self):
        self.head = Node(-1, None, None)
    def search(self, target: int) -> bool:
        cur=self.head
        while cur:
            while cur.next and cur.next.val<target:
                cur=cur.next
            if cur.next and cur.next.val==target:
                return True
            cur = cur.down
        return False
    def add(self, num: int) -> None:
        stack=[]
        cur=self.head
        while cur:
            while cur.next and cur.next.val<num:
                cur=cur.next
            stack.append(cur)
            cur = cur.down

        insert = True
        down = None
        while insert and stack:
            cur=stack.pop()
            node=Node(num,cur.next,down)
            cur.next=node
            down=node
            insert = random.random()<0.5

        if insert: # self.head has to be the highest
            self.head=Node(-1,None,self.head)
        return
    def erase(self, num: int) -> bool:
        cur=self.head
        found=False
        while cur:
            while cur.next and cur.next.val<num:
                cur=cur.next
            if cur.next and cur.next.val==num:
                found=True
                cur.next=cur.next.next
            cur=cur.down
        return found

class Tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='Skiplist':
                obj = get_sol()
                outputs.append(None)
            elif cmd=='search':
                outputs.append(obj.search(input[0]))
            elif cmd=='add':
                outputs.append(obj.add(input[0]))
            else:
                outputs.append(obj.erase(input[0]))
        return outputs
    def test_01(self):
        commands = ["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
        inputs=[[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]
        expected = [None, None, None, None, False, None, True, False, True, False]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
