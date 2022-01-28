from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(x): return LRUCache(x)
# https://www.youtube.com/watch?v=S6IfqDXWa10
# https://leetcode.com/problems/lru-cache/discuss/45926/Python-Dict-+-Double-LinkedList/553841

#### Solution 1 ####
class DLinkedNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    def __repr__(self):
        return str(self.key) + '->' + str(self.next)
class LRUCache:
    def __init__(self, capcacity: int):
        self.remain = capcacity
        self.di = {}
        self.head, self.tail = DLinkedNode(0, 0), DLinkedNode(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def put_last(self, node: DLinkedNode) -> None:
        p = self.tail.prev
        node.prev, node.next = p, self.tail
        p.next, self.tail.prev = node, node
        self.di[node.key]=node
    def remove(self, node: DLinkedNode) -> None:
        p, q = node.prev, node.next
        p.next, q.prev = q, p
        if node.key in self.di:
            self.di.pop(node.key)
    def get(self, key: int) -> int:
        if key not in self.di: return -1

        node = self.di[key]
        self.remove(node)
        self.put_last(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.di: # no of elements in the linked list will not change even if there are free spaces. Example: put(2,val) then put(2,val)
            self.remove(self.di[key])
        else:
            if self.remain:
                self.remain -= 1
            else:
                self.remove(self.head.next)

        node = DLinkedNode(key, value)
        self.di[key] = node
        self.put_last(node)



#### Without using head and tail node ####
class LRUCache2:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.prev = self.next = self

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = DLinkedNode(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.prev
        p.next = node
        self.prev = node
        node.prev = p
        node.next = self

# same as the first solution
class LRUCache3:
    def __init__(self, capacity: int):
        self.remain = capacity
        self.di = {}
        self.initialize()
    def __repr__(self):
        return self.di['head']
    def initialize(self):
        head = DLinkedNode('head', -1)
        tail = DLinkedNode('tail', -1)
        head.next = tail
        tail.prev = head
        self.di['head'] = head
        self.di['tail'] = tail
    def delete(self, node:DLinkedNode):
        if node.key not in self.di: return
        prev=node.prev
        next = node.next
        prev.next=next
        next.prev=prev
        self.di.pop(node.key)
    def add_last(self, node:DLinkedNode):
        tail = self.di['tail']
        prev = tail.prev
        node.next=tail
        node.prev=prev
        prev.next=node
        tail.prev=node
        self.di[node.key]=node
    def get(self, key: int) -> int:
        if key not in self.di: return -1
        node = self.di[key]
        val=node.val
        self.delete(node)
        self.add_last(DLinkedNode(key, val))
        return val
    def put(self, key: int, value: int) -> None:
        if key in self.di:
            node = self.di[key]
            self.delete(node)
            self.remain+=1
        if self.remain==0:
            self.delete(self.di['head'].next)
        else:
            self.remain-=1
        node = DLinkedNode(key, value)
        self.add_last(node)


class Tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='LRUCache': obj = get_sol(input[0]); outputs.append(None)
            elif cmd=='put': outputs.append(obj.put(input[0],input[1]))
            elif cmd=='get': outputs.append(obj.get(input[0]))
        return outputs
    def test01(self):
        commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        inputs=[     [2],    [1, 1], [2, 2], [1],  [3, 3], [2],  [4, 4], [1],   [3],  [4]]
        expected = [None,     None,    None,   1,    None,  -1,   None,   -1,     3,    4]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test02(self):
        commands = ["LRUCache","put","put","put","put","get","get"]
        inputs=[      [2],   [2,1],[1,1],[2,3],[4,1],  [1], [2]]
        expected = [   None,    None,None, None, None,  -1,   3]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test03(self):
        commands = ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
        inputs=[[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
        expected = [None,None,None,None,None,None,-1,None,19,17,None,-1,None,None,None,-1,None,-1,5,-1,12,None,None,3,5,5,None,None,1,None,-1,None,30,5,30,None,None,None,-1,None,-1,24,None,None,18,None,None,None,None,-1,None,None,18,None,None,-1,None,None,None,None,None,18,None,None,-1,None,4,29,30,None,12,-1,None,None,None,None,29,None,None,None,None,17,22,18,None,None,None,-1,None,None,None,20,None,None,None,-1,18,18,None,None,None,None,20,None,None,None,None,None,None,None]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test04(self):
        commands = ["LRUCache","put","put","get","put","put","get"]
        inputs=[[2],       [2,1],  [2,2], [2],  [1,1], [4,1],[2]]
        expected = [None, None, None, 2, None, None, -1]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test05(self):
        cache = get_sol(1)
        cache.put(2,1)
        a = cache.get(2)
        self.assertEqual(1,a)
