from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:return False
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast==slow:return True
        return False
    def hasCycle2(self, head: ListNode) -> bool:
        if not head:return False
        slow=head
        fast=head.next
        while True:
            if fast is None:return False
            if fast.next is None:return False
            if fast==slow:return True
            slow = slow.next
            fast = fast.next.next

def make_linked_list(li,i=0):
    if not li: return None
    if i==len(li)-1:return ListNode(li[i])
    cur = ListNode(li[i])
    cur.next = make_linked_list(li,i+1)
    return cur
def add_cycle(head,pos):
    if pos<0: return
    p1=p2=head
    if pos>=0:
        i=0
        while i<pos:
            p1=p1.next
            i+=1
        while p2.next:
            p2=p2.next
        p2.next=p1

class tester(unittest.TestCase):
    def test1(self):
        head = [3,2,0,-4]
        pos = 1
        Output = True
        new_head = make_linked_list(head)
        add_cycle(new_head,pos)
        self.assertEqual(Output,get_sol().hasCycle(new_head))
    def test2(self):
        head = [1,2]
        pos = 0
        Output= True
        new_head = make_linked_list(head)
        add_cycle(new_head,pos)
        self.assertEqual(Output,get_sol().hasCycle(new_head))
    def test03(self):
        head = [1]
        pos = -1
        Output= False
        new_head = make_linked_list(head)
        add_cycle(new_head,pos)
        self.assertEqual(Output,get_sol().hasCycle(new_head))
    def test04(self):
        head = []
        pos = -1
        Output= False
        new_head = make_linked_list(head)
        add_cycle(new_head,pos)
        self.assertEqual(Output,get_sol().hasCycle(new_head))
    def test05(self):
        head = [1,2]
        pos = -1
        Output= False
        new_head = make_linked_list(head)
        add_cycle(new_head,pos)
        self.assertEqual(Output,get_sol().hasCycle(new_head))
