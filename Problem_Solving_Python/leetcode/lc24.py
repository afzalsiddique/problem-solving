import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)+','+str(self.next)
    def __eq__(self, other):
        return str(self)==str(other)

# recursive without changing node values
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def helper(head):
            if not head: return
            if not head.next: return head # odd
            first,second=head,head.next
            res = helper(second.next)
            second.next=first
            first.next=res
            return second

        return helper(head)

# iterative without changing node values
class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return
        first,second=head,head.next
        if head.next:
            new_head=second
        else:
            new_head=first
        while first and second:
            nxt=second.next
            if second.next and second.next.next:
                first.next=second.next.next
            else:
                first.next=second.next
            second.next=first
            first=nxt
            second=None if not nxt else nxt.next
        return new_head

def make_linked_list(li,i=0):
    if i==len(li)-1:return ListNode(li[i])
    cur = ListNode(li[i])
    cur.next = make_linked_list(li,i+1)
    return cur

class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(make_linked_list([2,1,4,3]),Solution().swapPairs(make_linked_list([1,2,3,4])))
    def test2(self):
        self.assertEqual(make_linked_list([1]),Solution().swapPairs(make_linked_list([1])))
    def test3(self):
        self.assertEqual(make_linked_list([2,1]),Solution().swapPairs(make_linked_list([1,2])))
    def test4(self):
        self.assertEqual(make_linked_list([2,1,3]),Solution().swapPairs(make_linked_list([1,2,3])))
    def test5(self):
        self.assertEqual(make_linked_list([2,1,4,3,5]),Solution().swapPairs(make_linked_list([1,2,3,4,5])))
