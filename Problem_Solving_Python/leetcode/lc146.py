# https://www.youtube.com/watch?v=S6IfqDXWa10
# https://leetcode.com/problems/lru-cache/discuss/45926/Python-Dict-+-Double-LinkedList/553841
import unittest
#### Solution 1 ####
class DLinkedNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capcacity: int):
        self.remain = capcacity
        self.dict = {}
        self.head, self.tail = DLinkedNode(0, 0), DLinkedNode(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key not in self.dict: return -1

        node = self.dict[key]
        self.remove_node_from_linkedlist(node)
        self.add_node_to_linkedlist(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove_node_from_linkedlist(self.dict[key])
        else:
            if self.remain:
                self.remain -= 1
            else:
                p = self.head.next
                self.dict.pop(p.key)
                self.remove_node_from_linkedlist(p)

        node = DLinkedNode(key, value)
        self.dict[key] = node
        self.add_node_to_linkedlist(node)

    def add_node_to_linkedlist(self, node: DLinkedNode) -> None:
        p = self.tail.prev
        node.prev, node.next = p, self.tail
        p.next, self.tail.prev = node, node

    def remove_node_from_linkedlist(self, node: DLinkedNode) -> None:
        p, q = node.prev, node.next
        p.next, q.prev = q, p


#### Without using head and tail node ####
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

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
        n = Node(key, value)
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

class Case(unittest.TestCase):
    def test_1(self):
        cache = LRUCache(1)
        cache.put(2,1)
        a = cache.get(2)
        self.assertEqual(1,a)