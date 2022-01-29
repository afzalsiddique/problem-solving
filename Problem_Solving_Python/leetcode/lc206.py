import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution2()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val) + "->" + str(self.next)
class Solution:
    # iterative
    def reverseList(self, head: ListNode) -> ListNode:
        prev=None
        while head:
            nxt=head.next
            head.next=prev
            prev=head
            head=nxt
        return prev
class Solution4:
    # iterative 2. p=prev c=current n=next
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        dummy=ListNode(-9999,head)
        p=dummy
        c=p.next
        n=c.next
        while n:
            c.next=n.next
            n.next=p.next
            p.next=n
            n=c.next
        return dummy.next
# recursive
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if head==None:return None
        if head.next==None:
            return head # head will be the first node in the reversed list. so return first node
        first_node = self.reverseList(head.next)
        head.next.next = head
        head.next=None
        return first_node
class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        curr = head.next
        prev = head
        while curr!=None:
            curr.next, prev, curr = prev, curr, curr.next # this line is very bad. avoid this. Does not do the job simultaneously
        head.next = None # to avoid cycle
        return prev



class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(make_linked_list([5,4,3,2,1]), get_sol().reverseList(make_linked_list([1,2,3,4,5])))
    def test02(self):
        self.assertEqual(make_linked_list([2,1]), get_sol().reverseList(make_linked_list([1,2])))
    def test03(self):
        self.assertEqual(make_linked_list([]), get_sol().reverseList(make_linked_list([])))
    def test04(self):
        self.assertEqual(make_linked_list([1]), get_sol().reverseList(make_linked_list([1])))
