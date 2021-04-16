import pickle
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
        return str(self.val) + "->" + str(self.next)

# https://www.youtube.com/watch?v=meOY1wajrnw
class Solution:
    def reorderList(self, head):
        #step 1: find middle
        if not head: return
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        #step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        slow.next = None

        #step 3: merge lists
        head1, head2 = head, prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt


# using stack. time n. memory n.
class Solution2:
    def reorderList(self, head: ListNode) -> None:
        if not head: return
        st,size=[],0
        cur=head
        while cur:
            st.append(cur)
            size+=1
            cur=cur.next
        cur=head
        for _ in range(size//2):
            nxt=cur.next
            cur.next=st.pop()
            cur=cur.next
            cur.next=nxt
            cur=cur.next
        cur.next=None

def make_linked_list(li,i=0):
    if i==len(li)-1:return ListNode(li[i])
    cur = ListNode(li[i])
    cur.next = make_linked_list(li,i+1)
    return cur
class tester(unittest.TestCase):
    def test1(self):
        expected = make_linked_list([1,4,2,3])
        actual=make_linked_list([1,2,3,4])
        Solution().reorderList(actual)
        self.assertEqual(expected,actual)
    def test2(self):
        expected = make_linked_list([1,5,2,4,3])
        actual=make_linked_list([1,2,3,4,5])
        Solution().reorderList(actual)
        self.assertEqual(expected,actual)
    def test3(self):
        expected = make_linked_list([1,10,2,9,3,8,4,7,5,6])
        actual=make_linked_list([1,2,3,4,5,6,7,8,9,10])
        Solution().reorderList(actual)
        self.assertEqual(expected,actual)
    def test4(self):
        expected = make_linked_list([1,11,2,10,3,9,4,8,5,7,6])
        actual=make_linked_list([1,2,3,4,5,6,7,8,9,10,11])
        Solution().reorderList(actual)
        self.assertEqual(expected,actual)
