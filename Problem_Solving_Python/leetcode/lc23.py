from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from queue import PriorityQueue
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val) + "->" + str(self.next)
    def __eq__(self, other):
        return str(self)==str(other)

# heap
class Solution3:
    def mergeKLists(self, lists):
        class Wrapper:
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.data < other.Node.data
            def __repr__(self):
                return str(self.node.data) + "->" + str(self.node.next)

        dummy = ListNode(0)
        cur = dummy
        pq = []
        for head in lists:
            if head:
                heappush(pq, Wrapper(head))
        while pq:
            node = heappop(pq).Node
            cur.next = node
            cur=cur.next
            if node:
                node = node.next
                if node:
                    heappush(pq, Wrapper(node))
        return dummy.next

# priority queue
class Solution:
    def mergeKLists(self, lists):
        class Wrapper:
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.data < other.Node.data

        dummy = cur = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put(Wrapper(l))
        while not q.empty():
            node = q.get().Node
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

def make_linked_list(li:List) -> ListNode:
    """
    given a list the function creates a linked list and returns the head of the linked list
    """
    n = len(li)
    if n==0:
        return None
    if n==1:
        return ListNode(li[0])
    temp = ListNode(li[-1], None)
    for i in range(n-2,-1,-1):
        temp = ListNode(li[i],temp)
    return temp

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        lists=[]
        lists.append(make_linked_list([1,4,5]))
        lists.append(make_linked_list([1,3,4]))
        lists.append(make_linked_list([2,6]))
        actual = sol.mergeKLists(lists)
        expected = make_linked_list([1,1,2,3,4,4,5,6])
        self.assertEqual(expected, actual)
