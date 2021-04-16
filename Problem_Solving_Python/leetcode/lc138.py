from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List






class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
    def __repr__(self):
        return str(self.val)

class Solution:
    def copyRandomList(self, head: 'Node'):
        if not head:return None
        cur = head
        while cur:
            nxt=cur.next
            cur.next=Node(cur.val)
            cur.next.next=nxt
            cur=nxt
        cur=head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        new_head = head.next
        first, second=head,head.next
        while second.next:
            first.next=second.next
            first=second
            second=second.next
        # this also works
        # while second.next:
        #     first.next=second.next
        #     first=first.next
        #     second.next=first.next
        #     second=second.next
        return new_head
    # using dict
    def copyRandomList2(self, head: 'Node'):
        if not head:return None
        di = {}
        old_node=head
        while old_node:
            di[old_node]=Node(old_node.val)
            old_node=old_node.next
        old_node=head
        while old_node:
            if old_node.random:
                di[old_node].random=di[old_node.random]
            if old_node.next:
                di[old_node].next=di[old_node.next]
            old_node=old_node.next
        return di[head]

class MyTestClass(unittest.TestCase):
    def test_1(self):
        n1=Node(1)
        n10=Node(10,n1)
        n11=Node(11,n10)
        n13=Node(13,n11)
        n7=Node(7,n13)
        n13.random = n7
        n11.random = n10
        n10.random = n11
        n1.random = n7
        self.assertEqual("0", Solution().copyRandomList(n7))