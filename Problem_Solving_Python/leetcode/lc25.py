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
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        if not head.next: return head
        new_head = self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return new_head
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head: return
        if k==1: return head
        curr=head
        cnt=k-1
        while cnt and curr:
            cnt-=1
            curr=curr.next
        if not curr: return head
        nxt=curr.next
        curr.next=None
        new_head=self.reverseList(head)
        head.next=self.reverseKGroup(nxt,k)
        return new_head

def make_linked_list(li,i=0):
    if i==len(li)-1:return ListNode(li[i])
    cur = ListNode(li[i])
    cur.next = make_linked_list(li,i+1)
    return cur


class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(make_linked_list([2,1,4,3]),Solution().reverseKGroup(make_linked_list([1,2,3,4]),2))
    def test2(self):
        self.assertEqual(make_linked_list([3,2,1,6,5,4]),Solution().reverseKGroup(make_linked_list([1,2,3,4,5,6]),3))
    def test3(self):
        self.assertEqual(make_linked_list([3,2,1,6,5,4,7,8]),Solution().reverseKGroup(make_linked_list([1,2,3,4,5,6,7,8]),3))
    def test4(self):
        self.assertEqual(make_linked_list([1,2,3,4,5]),Solution().reverseKGroup(make_linked_list([1,2,3,4,5]),1))