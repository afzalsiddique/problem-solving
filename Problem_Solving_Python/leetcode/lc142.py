import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self): return str(self.val)

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return None
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        if not fast or not fast.next: return None
        fast=head
        while fast!=slow:
            fast=fast.next
            slow=slow.next
        return fast

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
    return p1 # return starting node of the cycle

class tester(unittest.TestCase):
    def test1(self):
        head = [3,2,0,-4]
        pos = 1
        new_head = make_linked_list(head)
        Output = add_cycle(new_head,pos)
        self.assertEqual(Output,get_sol().detectCycle(new_head))
    def test2(self):
        head = [1,2]
        pos = 0
        new_head = make_linked_list(head)
        Output = add_cycle(new_head,pos)
        self.assertEqual(Output,get_sol().detectCycle(new_head))
    def test03(self):
        head = [1]
        pos = -1
        new_head = make_linked_list(head)
        Output = add_cycle(new_head,pos)
        self.assertEqual(Output,get_sol().detectCycle(new_head))
    def test04(self):
        head = []
        pos = -1
        new_head = make_linked_list(head)
        Output = add_cycle(new_head,pos)
        self.assertEqual(Output,get_sol().detectCycle(new_head))
    def test05(self):
        head = [1,2]
        pos = -1
        new_head = make_linked_list(head)
        Output = add_cycle(new_head,pos)
        self.assertEqual(Output,get_sol().detectCycle(new_head))
