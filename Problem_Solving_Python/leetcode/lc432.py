import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return AllOne()
class Node:
    def __init__(self):
        self.key_set = set([])
        self.prev, self.nxt = None, None
    def __repr__(self): return str(self.key_set)

    def add_key(self, key:str):
        self.key_set.add(key)

    def remove_key(self, key:str):
        self.key_set.remove(key)

    def get_any_key(self):
        if self.key_set:
            result = self.key_set.pop()
            self.add_key(result)
            return result
        else:
            return None

    def count(self):
        return len(self.key_set)

    def is_empty(self):
        return len(self.key_set) == 0


class DoubleLinkedList:
    def __init__(self):
        self.head_node, self.tail_node = Node(), Node()
        self.head_node.nxt, self.tail_node.prev = self.tail_node, self.head_node
        return

    def insert_after(self, x:Node):
        node, temp = Node(), x.nxt
        x.nxt, node.prev = node, x
        node.nxt, temp.prev = temp, node
        return node

    def insert_before(self, x:Node):
        return self.insert_after(x.prev)

    def remove(self, x:Node):
        prev_node = x.prev
        prev_node.nxt, x.nxt.prev = x.nxt, prev_node
        return

    def get_head(self):
        return self.head_node.nxt

    def get_tail(self):
        return self.tail_node.prev

    def get_sentinel_head(self):
        return self.head_node

    def get_sentinel_tail(self):
        return self.tail_node
    def __repr__(self):
        li = []
        node = self.get_head()
        while node!=self.get_sentinel_tail():
            li.append(str(node.key_set))
            node=node.nxt
        # else:
        #     li.append('nothing')
        return '->'.join(li)

class AllOne:
    def __init__(self):
        self.dll=DoubleLinkedList()
        self.nodes={0:self.dll.get_sentinel_head()} # (key,val)=(freq,Node)
        self.counter=Counter()
    def remove_prev_freq(self, prev_freq, key):
        if prev_freq==0: return
        node=self.nodes[prev_freq]
        node.remove_key(key)
        if node.is_empty():
            self.dll.remove(node)
            self.nodes.pop(prev_freq)
        return
    def inc(self, key: str) -> None:
        nodes,counter=self.nodes,self.counter

        prev_freq=counter[key]
        counter[key]+=1
        cur_freq=counter[key]

        if cur_freq not in nodes:
            new_node=self.dll.insert_after(nodes[prev_freq])
            nodes[cur_freq]=new_node

        nodes[cur_freq].add_key(key)
        print(self.dll)
        self.remove_prev_freq(prev_freq,key)
        return
    def dec(self, key: str) -> None:
        nodes,counter=self.nodes,self.counter

        prev_freq=counter[key]
        counter[key]-=1
        cur_freq=counter[key]

        if cur_freq not in nodes:
            node=self.dll.insert_before(nodes[prev_freq])
            nodes[cur_freq]=node

        if cur_freq!=0:
            nodes[cur_freq].add_key(key)
        print(self.dll)
        self.remove_prev_freq(prev_freq,key)
        return
    def getMaxKey(self) -> str:
        return self.dll.get_tail().get_any_key() if self.dll.get_tail().count() > 0 else ""
    def getMinKey(self) -> str:
        return self.dll.get_head().get_any_key() if self.dll.get_head().count() > 0 else ""

class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='AllOne':
                obj = get_sol()
                outputs.append(None)
            elif cmd=='inc':
                outputs.append(obj.inc(input[0]))
            elif cmd=='dec':
                outputs.append(obj.dec(input[0]))
            elif cmd=='getMaxKey':
                outputs.append(obj.getMaxKey())
            else:
                outputs.append(obj.getMinKey())
        return outputs
    def test_01(self):
        commands = ["AllOne", "inc",   "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
        inputs=[       [], ["hello"], ["hello"], [],         [],       ["leet"],   [],        []]
        expected = [None,   None,     None,    "hello",     "hello",    None,    "hello",    "leet"]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_02(self):
        commands = ["AllOne","inc","inc","inc", "inc","inc", "dec","dec","getMaxKey","getMinKey"]
        inputs=[     [],    ["a"], ["b"], ["b"],["b"],["b"], ["b"],["b"],   [],        []]
        expected = [None,   None,  None,  None,  None,  None,None, None,   "b",        "a"]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_03(self):
        commands = ["AllOne","inc","inc","inc","inc","inc","inc","dec", "dec","getMinKey","dec","getMaxKey","getMinKey"]
        inputs=[      [],    ["a"],["b"],["b"],["c"],["c"],["c"],["b"],["b"],    [],     ["a"],   [],         []]
        expected = [None,   None,  None, None, None, None, None, None, None,    "a",    None,    "c",        "c"]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)

