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

    def put_last(self, node: DLinkedNode) -> None:
        p = self.tail.prev
        node.prev, node.next = p, self.tail
        p.next, self.tail.prev = node, node

    def remove(self, node: DLinkedNode) -> None:
        p, q = node.prev, node.next
        p.next, q.prev = q, p
    def get(self, key: int) -> int:
        if key not in self.dict: return -1

        node = self.dict[key]
        self.remove(node)
        self.put_last(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])
        else:
            if self.remain:
                self.remain -= 1
            else:
                p = self.head.next
                self.dict.pop(p.val)
                self.remove(p)

        node = DLinkedNode(key, value)
        self.dict[key] = node
        self.put_last(node)



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
            return n.data
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

# same as the first solution
class ListNode:
    def __init__(self,key,val,prev=None,next=None):
        self.key=key
        self.val=val
        self.prev = prev
        self.next=next
    def __repr__(self):
        return str(self.key) + '->' + str(self.next)
class LRUCache:
    def __init__(self, capacity: int):
        self.remain = capacity
        self.di = {}
        self.initialize()
    def __repr__(self):
        return self.di['head']
    def initialize(self):
        head = ListNode('head',-1)
        tail = ListNode('tail',-1)
        head.next = tail
        tail.prev = head
        self.di['head'] = head
        self.di['tail'] = tail
    def delete(self,node:ListNode):
        if node.key not in self.di: return
        prev=node.prev
        next = node.next
        prev.next=next
        next.prev=prev
        self.di.pop(node.key)
    def add_last(self,node:ListNode):
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
        self.add_last(ListNode(key,val))
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
        node = ListNode(key,value)
        self.add_last(node)

class tester(unittest.TestCase):
    def test_1(self):
        cache = LRUCache(1)
        cache.put(2,1)
        a = cache.get(2)
        self.assertEqual(1,a)
    def test2(self):
        commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        inputs = [     [2],    [1, 1], [2, 2], [1],  [3, 3], [2],  [4, 4], [1],   [3],  [4]]
        exptected = [None,     None,    None,   1,    None,  -1,   None,   -1,     3,    4]
        outputs = []
        for c,i in zip(commands, inputs):
            if c == 'LRUCache':
                obj = LRUCache(i[0])
                outputs.append(None)
            elif c =='put':
                outputs.append(obj.put(i[0],i[1]))
            elif c=='get':
                outputs.append(obj.get(i[0]))
        self.assertEqual(exptected,outputs)
    def test3(self):
        commands = ["LRUCache","put","put","put","put","get","get"]
        inputs = [      [2],   [2,1],[1,1],[2,3],[4,1],  [1], [2]]
        exptected = [   None,    None,None, None, None,  -1,   3]
        outputs = []
        for c,i in zip(commands, inputs):
            if c == 'LRUCache':
                obj = LRUCache(i[0])
                outputs.append(None)
            elif c =='put':
                outputs.append(obj.put(i[0],i[1]))
            elif c=='get':
                outputs.append(obj.get(i[0]))
        self.assertEqual(exptected,outputs)
    def test4(self):
        commands = ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
        inputs = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
        exptected = [None,None,None,None,None,None,-1,None,19,17,None,-1,None,None,None,-1,None,-1,5,-1,12,None,None,3,5,5,None,None,1,None,-1,None,30,5,30,None,None,None,-1,None,-1,24,None,None,18,None,None,None,None,-1,None,None,18,None,None,-1,None,None,None,None,None,18,None,None,-1,None,4,29,30,None,12,-1,None,None,None,None,29,None,None,None,None,17,22,18,None,None,None,-1,None,None,None,20,None,None,None,-1,18,18,None,None,None,None,20,None,None,None,None,None,None,None]
        outputs = []
        for c,i in zip(commands, inputs):
            if c == 'LRUCache':
                obj = LRUCache(i[0])
                outputs.append(None)
            elif c =='put':
                outputs.append(obj.put(i[0],i[1]))
            elif c=='get':
                outputs.append(obj.get(i[0]))
        self.assertEqual(exptected,outputs)
