from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution3()
from queue import PriorityQueue

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self): return str(self.val) + "->" + str(self.next)
    def __eq__(self, other): return str(self)==str(other)

class Solution3:
    # heap
    def mergeKLists(self, lists):
        class Wrapper:
            def __init__(self, node): self.node = node
            def __lt__(self, other): return self.node.val < other.node.val
            def __repr__(self): return str(self.node.data) + "->" + str(self.node.next)

        dummy = ListNode(0)
        cur = dummy
        pq = []
        for head in lists:
            if head: heappush(pq, Wrapper(head))
        while pq:
            node = heappop(pq).node
            cur.next = node
            cur=cur.next
            if node and node.next:
                heappush(pq, Wrapper(node.next))
        return dummy.next
class Solution4:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        cur=dummy
        pq=[]
        for h in lists:
            if h: heappush(pq,[h.val,random.random(),h]) # insert random value to avoid comparsion between nodes
        while pq:
            _,_,node=heappop(pq)
            if node.next:
                heappush(pq,[node.next.val,random.random(),node.next])
            node.next=None
            cur.next=node
            cur=cur.next
        return dummy.next
class Solution:
    # priority queue
    def mergeKLists(self, lists):
        class Wrapper:
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.data < other.TrieNode.data

        dummy = cur = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put(Wrapper(l))
        while not q.empty():
            node = q.get().TrieNode
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                q.put(Wrapper(node))
        return dummy.next

# time O(kN). k is no of linked list and N is total nodes
class Solution2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy=ListNode(0)
        cur=dummy
        while True:
            lists = [head for head in lists if head if head]
            if len(lists)==0:break
            small,idx=float('inf'),0
            for i in range(len(lists)):
                if lists[i].val<small:
                    small=lists[i].val
                    idx=i
            cur.next=lists[idx]
            lists[idx] = lists[idx].next
            cur=cur.next
        return dummy.next


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(make_linked_list([1,1,2,3,4,4,5,6]),get_sol().mergeKLists(list(map(make_linked_list,[[1,4,5],[1,3,4],[2,6]]))))
    def test02(self):
        self.assertEqual(make_linked_list([]),get_sol().mergeKLists(list(map(make_linked_list,[[]]))))
    def test03(self):
        self.assertEqual(make_linked_list([]),get_sol().mergeKLists(list(map(make_linked_list,[]))))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
    # def test11(self):
    # def test12(self):
